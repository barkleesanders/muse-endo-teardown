# Muse "Endo" teardown — Meta's desktop agent has computer‑use built in, gated off

A static teardown of Meta's **Muse** desktop app for macOS (codename **"Endo"**, bundle
`com.meta.endo`, v1.0). The finished implementation for a computer‑using agent — seeing the
screen, clicking, typing, running programs, driving a browser — ships in the public build but is
switched **off** by server‑delivered feature flags.

> **Found in code, not shipped.** Everything here was read out of the released binary and its
> Meta‑served config on a single Mac. Flag names, gates, and plans change; some features never
> leave the lab. This is observation and commentary, not confirmation from Meta. No app binary is
> redistributed here, and no credentials are published.

**Read the illustrated report:** [`report/endo-edition-2026-09-17.pdf`](report/endo-edition-2026-09-17.pdf)

**Transport + attestation review (2026‑09‑28):** [`report/muse-cvm-attestation-security-review-2026-09-28.pdf`](report/muse-cvm-attestation-security-review-2026-09-28.pdf) — how the Mac reaches the cloud VM (Noise‑framed HTTP) and the SEV‑SNP attestation gate that lets a session originate. See [the section below](#the-cloud-vms-front-door--transport-framing-and-the-attestation-gate).

---

## Subject

| | |
|---|---|
| App | Muse (Meta) for macOS, v1.0 |
| Codename / bundle | Endo / `com.meta.endo` |
| Binary | Mach‑O arm64, ~17 MB, Swift + AppKit + SwiftUI |
| Signature | Developer ID Application: Meta Platforms, Inc. (notarized) |
| Updater | Sparkle |

## The five gated capability flags

Muse fetches its feature gates from a Meta config (`endo-values-public…json`, in the app's cache)
and **re‑downloads them on every launch** — editing them locally is overwritten within seconds.
Five booleans in the `hatch_desktop` namespace decide whether the agent can operate the machine,
and all five arrive `false`:

| Flag | Value | Governs |
|---|---|---|
| `hatch_desktop:enable_computer_control` | `false` | Clicking / typing / controlling the Mac |
| `hatch_desktop:endo_enable_screen_recording` | `false` | The agent seeing the screen |
| `hatch_desktop:enable_browser_automation` | `false` | Driving a browser |
| `hatch_desktop:endo_system_run_sandbox_enabled` | `false` | Sandboxed program execution |
| `hatch_desktop:endo_enable_computer_use_onboarding` | `false` | First‑run "let Muse control your Mac" flow |

## What the binary already contains behind those flags

- **Screen vision** — links Apple's `ScreenCaptureKit` (`SCShareableContent`, `SCStreamConfiguration`),
  calls `CGPreflightScreenCaptureAccess` / `CGRequestScreenCaptureAccess`, and carries an on‑screen
  computer‑use overlay + an accessibility‑first click mode (`_showComputerUseOverlay`,
  `_preferAXForComputerUseClicks`, `[ComputerUse] Display assertion acquired`).
- **Program execution** — a `system.run` primitive: *"Execute a single program with argv‑style
  arguments. Shell operators, redirects, pipes, globbing, and environment expansion are not
  supported."* AppleScript (`osascript`/`osacompile`) and `open -a` app launches are explicitly
  rejected in background mode. Deliberately narrow — an execution primitive built for a careful
  rollout, not a shell.
- **Session control** — `computer.session` (start/end, once per request) and `computer.control`.
- **Browser automation** — Chromium over the DevTools Protocol on loopback
  (`--remote-debugging-address=127.0.0.1`).
- **Voice** — dictation via "Voyager" (`wss://shortwave.facebook.com/voyager/v1/asr/duplex`,
  model `prod_hatch_macos`) and a duplex speech‑to‑speech engine "Alo" (`aloS2SModelId`), with a
  named voice `avocado_v2:MAI_02` and a push‑to‑talk flag (`enable_ptt_s2s`).

## What already works today (the live device‑command catalog)

With computer‑use gated off, the agent still exposes a **51‑command** catalog on a permissioned
Mac — none of which is screen capture, clicking, typing, or shell:

```
calendar.create/delete/search/update      reminders.create/complete/delete/list/update
contacts.create/delete/search/update      notes.append/create/delete/folders/list/read/search/update
email.read/search/send/delete/status      imessage.send/search/threads/attachment/save
files.read/write/edit/copy/rename/trash/upload/search/mkdir/list
camera.snap   whatsapp.search   media_library.sync   system.notify
environment.describe   connection.health/repair   data_source.search
```

## Architecture — why a local flag flip can't force it on

The agent does not run on the Mac. It runs in a **per‑user Meta cloud VM** reached over a
Noise‑encrypted WebSocket gateway; the Mac is a set of hands, the reasoning is server‑side. So the
tool catalog is provisioned by Meta's backend, and the gate is enforced end‑to‑end — no local
config edit or firewall rule enables computer‑use.

| Role | Host / component |
|---|---|
| Per‑user agent VM | `hatch.metaaivm.com` |
| Chat / agent API + config | `hatch-api.meta.ai`, `api.meta.ai` |
| Transport | Tigon HTTP client · Noise‑encrypted `wss` gateway |
| Auth backend | Meta "Proton" (`api.meta.ai/proton/…`) |
| Edge | `edge-metaclaw-http.c10r.facebook.com` |

## The tell: staged, employee‑first rollout

Two flags in the same config give the plan away: an onboarding walkthrough that is **built but
hidden** (`endo_enable_computer_use_onboarding`) and an **employee** switch shipped in the public
build (`voyager_is_employee`). Consistent with internal testing now, ahead of a cohort rollout.

## The cloud VM's front door — transport framing and the attestation gate

A follow‑up review looked at *how* the Mac talks to that per‑user cloud VM, and at the
control that decides whether a connection is allowed to originate at all. Findings only —
no gate was defeated and no signed loader was patched; this is DMCA §1201(f) interoperability
observation of software on a Mac the author owns.

**Read the review:** [`report/muse-cvm-attestation-security-review-2026-09-28.pdf`](report/muse-cvm-attestation-security-review-2026-09-28.pdf)

- **Transport is HTTP‑over‑Noise, in two protobuf layers.** The session is a
  `Noise_XX_25519_AESGCM_SHA256` handshake over `wss://<vm>.metaaivm.com/v1/noise`. Inside it,
  an inner envelope (`hatch.noise`) carries an `ApplicationRequest{verb, path, headers, body}` —
  ordinary HTTP requests tunnelled through the encrypted channel — and an outer transport frame
  (`ingress_rev_proxy.NoiseTransportFrame{chunk_id, chunk_index, total_chunks, payload}`) splits a
  message into ≤65,489‑byte chunks (≤256 of them), each encrypted on the split‑transmit cipher.
- **The gate is remote attestation, not a client secret.** A verifier
  (`SnpAttestationVerifier`, AMD SEV‑SNP; Milan/Genoa/Turin) checks the VM's attestation report:
  the report_data is bound to the handshake (`SHA‑256(binding) == reportData[0:32]`, upper half
  zero), a structural hardware policy is enforced (`allowDebug:false`, `requiredVmpl:0`, TCB
  floors, `allowMigration:false`, SMT denied, page‑swap/alias checks required), and the cert
  manifest must be Cloudflare‑endorsed, un‑revoked, and fresh.
- **What `verify()` accepts.** There is **no pinned measurement hash** — it accepts *any* genuine
  SEV‑SNP VM that meets the hardware floor and presents an endorsed, un‑revoked, handshake‑bound
  manifest. The client‑side check is tier‑gated by a MobileConfig flag
  (`hatch_web:attestation_enforce_mode`, default `0`/Off); the real barrier for an external client
  is **server‑side and cryptographic** — a signed `auth_token` + `notary_token` plus a handshake
  against the CVM's genuine static key, none of which a local flag flip or client patch can mint.
- **Consequence.** Every method is reachable *inside* an attested session, but originating one
  from an outside client requires server‑held signing keys, not a bypassable local gate. The
  supported interop paths remain a browser‑backed shim and native paste‑and‑click.

CVM/transport figures measured on **2026‑09‑28**.

## Method

- Static read of the shipping binary's linked symbols and strings.
- Read of the app's own Meta‑served feature‑config cache.
- Enumeration of the agent's exposed device‑command catalog on a permissioned Mac.
- Launch‑time DNS capture to identify the endpoints (hostnames only; no traffic decryption).

No credentials, tokens, or personal data are included in this repository, and no Meta binary is
redistributed. All figures are measured, not estimated, on **2026‑09‑17**.
