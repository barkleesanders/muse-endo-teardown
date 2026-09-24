# /decompile — Muse (Endo) Mac client static analysis

Reverse-engineer the Meta Muse Mac app (bundle id `com.meta.endo`) to learn what it
ships: feature flags, client defaults, config endpoints, and gated flows. Reproducible
from the public installer — no account, no auth, no live server needed.

## 0. Ground-truth discipline

- Client code shows what the app *can* do and each flag's *client default*. It never
  shows the live server-side value. A flag defaulting to `false` with a remote
  override is **not** evidence the feature is on or off for any user.
- Never claim a feature is live from static inspection alone. The reporting record
  format from prior work: finding / how verified / what it does NOT establish.
- Record the exact build analyzed: version + build number + SHA-256 of the DMG.

## 1. Get the installer

- The app self-updates via Sparkle. The feed URL is in the installed app's
  `Contents/Info.plist` under `SUFeedURL`
  (currently `https://www.facebook.com/endo/release/appcast.xml?channel=production`).
- Fetch the appcast, take the latest `<enclosure>` URL — that is the DMG download.
  Fallback: the official download page linked from Meta's Muse product site.
- Verify integrity: `shasum -a 256 Muse-*.dmg` and compare against any published
  value (e.g. RuntimeWire published `3db5892d…2eec49` for Muse-2.2.dmg).

## 2. Extract

On a Mac:

```sh
hdiutil attach Muse-2.2.dmg -nobrowse -readonly -mountpoint /tmp/muse-dmg
cp -R /tmp/muse-dmg/Muse.app /tmp/Muse.app
hdiutil detach /tmp/muse-dmg
```

On Linux (no hdiutil): `7z x Muse-2.2.dmg -o/tmp/muse-dmg` (HFS+/APFS extraction
via 7z; the app bundle survives — only the code signature is irrelevant for
static reads).

## 3. Analyze — the high-value targets, in order

1. **`Muse.app/Contents/Resources/hatch/metaconfig.json`** — the client-side flag
   registry. Maps 8-hex-char parameter IDs to `namespace:key` entries with types
   (`boolean` / `string` / `number`). This is the authoritative list of flags the
   bundled web client knows about. (2.2 shipped 44: 39 `hatch_web:`, 3
   `hatch_gtm:`, 1 `hatch_config:`, 1 `mwa_help_and_support:`.)
2. **`Muse.app/Contents/Resources/hatch/index.html`** (~50 MB bundled web client) —
   grep for each flag key to find its client default and the gated UI:
   `grep -o 'hatch_web:[a-z_0-9]*' index.html | sort -u`. A route that is removed
   from navigation and returns not-found when its flag is off = flag-gated flow.
3. **`Muse.app/Contents/MacOS/Muse`** (native binary, ~17 MB) — `strings` it for
   the *desktop-native* flags, which live outside metaconfig.json:
   `strings Muse | grep -o 'hatch_desktop:[a-z_]*' | sort -u`
   Also grep for `endo-values`, `MobileConfig`, and config-fetch URL patterns to
   find where the server-side gate values are downloaded and cached.
4. **`Muse.app/Contents/Info.plist`** — `CFBundleShortVersionString`,
   `CFBundleVersion` (build), `SUFeedURL` (update channel). Always report these
   with findings.
5. **Live prefs** `~/Library/Preferences/com.meta.endo.plist` (binary plist —
   `plutil -p` or Python `plistlib`) — shows migration markers
   (`endo_migrated.*`), permission-asked state (`endo_system_permission_asked.*`),
   and onboarding state. No server flag values live here.

## 4. What prior runs found (2.2, build 1074644564)

- `hatch_web:muse_mail` (boolean, client default false): gates a CreateMailboxSection
  flow for an agent-owned `@muse.ai` address, with Received/Sent views and
  attachment handling in the bundled client. Server value unknown — not live per
  static inspection alone.
- `hatch_desktop:enable_computer_control`, `hatch_desktop:endo_enable_screen_recording`,
  `hatch_desktop:enable_browser_automation`,
  `hatch_desktop:endo_system_run_sandbox_enabled`,
  `hatch_desktop:endo_enable_computer_use_onboarding` (from the v1.0 teardown):
  server-side gates, re-downloaded on every launch; no local representation in 2.2.
- Full 2.2 flag table: `findings/flag-registry-2.2.md`.

## 5. Limits

- device bridges (Muse `device.invoke` `files.upload`) cap uploads at 50 MB —
  `index.html` (~53 MB) cannot be pulled that way; analyze it on a Mac with
  shell access, or pull `metaconfig.json` (4 KB) for the flag list alone.
- `~/Library/HTTPStorages/com.meta.endo/` (the app's HTTP cache) may hold the
  fetched server config, but it is not readable through the device file bridge.
- Re-run this skill on every new public build; flags get added, renamed, and
  re-namespaced between versions (v1.0's on-disk `endo-values-public-*.json`
  cache is gone in 2.2).
