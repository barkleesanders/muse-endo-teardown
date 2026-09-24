#!/usr/bin/env python3
"""Check Meta's Sparkle appcast for a new Muse Mac release.

Reads the last-analyzed version from findings/LATEST_VERSION (state file in
the repo). Compares against the newest <item> in the appcast. If newer, emits
GITHUB_OUTPUT variables: new_version, dmg_url.

No side effects when there is no new version.
"""
import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET

APPCAST_URL = "https://www.facebook.com/endo/release/appcast.xml?channel=production"
STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "../../findings/LATEST_VERSION")


def current_version():
    try:
        with open(STATE_FILE) as f:
            return f.read().strip()
    except FileNotFoundError:
        return ""


def parse_version(v):
    # "2.2" -> (2, 2); build numbers compared separately if needed
    return tuple(int(x) for x in re.findall(r"\d+", v))


def main():
    req = urllib.request.Request(
        APPCAST_URL,
        headers={"User-Agent": "Sparkle/2.0 (muse-decompile-watch)"},
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        xml = resp.read()

    root = ET.fromstring(xml)
    items = root.findall(".//item")
    if not items:
        print("No items in appcast", file=sys.stderr)
        return

    # Sparkle appcasts list newest first
    latest = items[0]
    title = (latest.findtext("title") or "").strip()
    enclosure = latest.find("enclosure")
    dmg_url = (enclosure.get("url") if enclosure is not None else "").strip()
    version_el = latest.find("{http://www.andymatuschak.org/xml-namespaces/sparkle}version")
    version = (version_el.text.strip() if version_el is not None and version_el.text
               else title)

    cur = current_version()
    print(f"appcast latest: {version} ({title})")
    print(f"repo state: {cur or '(none)'}")

    new_version = ""
    if dmg_url and (not cur or parse_version(version) > parse_version(cur)):
        new_version = version
        print(f"NEW RELEASE: {version} -> {dmg_url}")

    out = os.environ.get("GITHUB_OUTPUT")
    if out:
        with open(out, "a") as f:
            f.write(f"new_version={new_version}\n")
            f.write(f"dmg_url={dmg_url}\n")


if __name__ == "__main__":
    main()
