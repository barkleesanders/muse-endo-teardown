#!/usr/bin/env python3
"""Full static analysis of a Muse Mac DMG — "no hidden things".

Usage: analyze.py <dmg_url> <version>

Pipeline:
  1. Download the DMG, record SHA-256.
  2. Extract with 7z.
  3. Locate Muse.app inside.
  4. metaconfig.json -> findings/flag-registry-<version>.md (full flag table).
  5. Native binary strings -> findings/desktop-flags-<version>.md
     (hatch_desktop:* / hatch_web:* / config-endpoint strings).
  6. Info.plist -> version, build, channel recorded in the report header.
  7. Diff flag tables vs the previous version -> findings/diff-<prev>-to-<version>.md.
  8. Update findings/LATEST_VERSION.

Writes only under findings/. Exits non-zero on any failure so the workflow
never commits a partial analysis.
"""
import hashlib
import json
import os
import plistlib
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request

REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../..")
FINDINGS = os.path.join(REPO, "findings")


def run(cmd, **kw):
    return subprocess.run(cmd, check=True, capture_output=True, text=True, **kw)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def find_app(root):
    for dirpath, dirnames, _ in os.walk(root):
        if "Muse.app" in dirnames:
            return os.path.join(dirpath, "Muse.app")
    raise RuntimeError("Muse.app not found in extracted DMG")


def main():
    dmg_url, version = sys.argv[1], sys.argv[2]
    os.makedirs(FINDINGS, exist_ok=True)

    prev = ""
    state = os.path.join(FINDINGS, "LATEST_VERSION")
    if os.path.exists(state):
        prev = open(state).read().strip()

    tmp = tempfile.mkdtemp(prefix="muse-decompile-")
    dmg_path = os.path.join(tmp, f"Muse-{version}.dmg")
    print(f"Downloading {dmg_url}")
    req = urllib.request.Request(dmg_url, headers={"User-Agent": "Sparkle/2.0"})
    with urllib.request.urlopen(req, timeout=300) as r, open(dmg_path, "wb") as f:
        shutil.copyfileobj(r, f)
    digest = sha256_file(dmg_path)
    print(f"SHA-256: {digest}")

    out = os.path.join(tmp, "extracted")
    run(["7z", "x", dmg_path, f"-o{out}", "-y"])
    app = find_app(out)
    print(f"Muse.app at {app}")

    # --- Info.plist: version / build / channel ---
    with open(os.path.join(app, "Contents/Info.plist"), "rb") as f:
        info = plistlib.load(f)
    short = info.get("CFBundleShortVersionString", version)
    build = info.get("CFBundleVersion", "?")
    feed = info.get("SUFeedURL", "?")

    # --- metaconfig.json: the client flag registry ---
    mc_path = os.path.join(app, "Contents/Resources/hatch/metaconfig.json")
    with open(mc_path) as f:
        mc = json.load(f)
    flags = sorted((v["key"], v["type"], k)
                   for k, v in mc["clientParameters"].items())

    reg_lines = [
        f"# Muse {short} client flag registry",
        "",
        f"Build {build}, production channel. DMG SHA-256: `{digest}`.",
        "Source: `Muse.app/Contents/Resources/hatch/metaconfig.json`.",
        "Client defaults live in the bundled JS; server-side values are not",
        "visible statically — see the /decompile skill ground-truth rule.",
        "",
        "| parameter id | flag key | type |",
        "|---|---|---|",
    ]
    reg_lines += [f"| `{pid}` | `{key}` | {typ} |" for key, typ, pid in flags]
    reg_lines += ["", f"Total: {len(flags)} flags.", ""]
    reg_path = os.path.join(FINDINGS, f"flag-registry-{short}.md")
    open(reg_path, "w").write("\n".join(reg_lines))
    print(f"Wrote {reg_path} ({len(flags)} flags)")

    # --- native binary strings: desktop-native flags + endpoints ---
    binary = os.path.join(app, "Contents/MacOS/Muse")
    strings_out = run(["strings", binary]).stdout
    patterns = {
        "hatch_desktop flags": r"hatch_desktop:[A-Za-z0-9_]+",
        "hatch_web flags": r"hatch_web:[A-Za-z0-9_]+",
        "config/cache refs": r"[A-Za-z0-9_./-]*[Ee]ndo-?[Vv]alues[A-Za-z0-9_./-]*",
        "mobileconfig refs": r"[A-Za-z0-9_./-]*[Mm]obile[Cc]onfig[A-Za-z0-9_./-]*",
    }
    desk_lines = [
        f"# Muse {short} native binary findings",
        "",
        f"Build {build}. Extracted via `strings` on `Contents/MacOS/Muse`.",
        "These are string references, not proof of behavior.",
        "",
    ]
    for title, pat in patterns.items():
        hits = sorted(set(re.findall(pat, strings_out)))
        desk_lines.append(f"## {title} ({len(hits)})")
        desk_lines += [f"- `{h}`" for h in hits] or ["- (none found)"]
        desk_lines.append("")
    desk_path = os.path.join(FINDINGS, f"desktop-flags-{short}.md")
    open(desk_path, "w").write("\n".join(desk_lines))
    print(f"Wrote {desk_path}")

    # --- diff vs previous version ---
    if prev and prev != short:
        prev_reg = os.path.join(FINDINGS, f"flag-registry-{prev}.md")
        diff_lines = [f"# Flag diff: {prev} -> {short}", ""]
        if os.path.exists(prev_reg):
            prev_flags = {}
            for line in open(prev_reg):
                m = re.match(r"\| `([0-9a-f]+)` \| `([^`]+)` \| (\w+) \|", line)
                if m:
                    prev_flags[m.group(2)] = (m.group(1), m.group(3))
            cur_flags = {k: (pid, t) for k, t, pid in flags}
            added = sorted(set(cur_flags) - set(prev_flags))
            removed = sorted(set(prev_flags) - set(cur_flags))
            changed = sorted(k for k in set(cur_flags) & set(prev_flags)
                             if cur_flags[k] != prev_flags[k])
            diff_lines.append(f"## Added ({len(added)})")
            diff_lines += [f"- `{k}` ({cur_flags[k][1]})" for k in added] or ["- none"]
            diff_lines.append(f"## Removed ({len(removed)})")
            diff_lines += [f"- `{k}`" for k in removed] or ["- none"]
            diff_lines.append(f"## Changed ({len(changed)})")
            diff_lines += [f"- `{k}`" for k in changed] or ["- none"]
        else:
            diff_lines.append(f"No previous registry for {prev}; full table is new.")
        diff_lines.append("")
        diff_path = os.path.join(FINDINGS, f"diff-{prev}-to-{short}.md")
        open(diff_path, "w").write("\n".join(diff_lines))
        print(f"Wrote {diff_path}")

    # --- state ---
    open(state, "w").write(short + "\n")
    print(f"State updated: LATEST_VERSION={short}")

    shutil.rmtree(tmp, ignore_errors=True)
    print("Analysis complete — no hidden steps, all outputs under findings/.")


if __name__ == "__main__":
    main()
