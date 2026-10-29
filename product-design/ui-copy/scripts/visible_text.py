#!/usr/bin/env python3
"""List every line of text a person will see in a rendered HTML mockup.

Usage: python3 visible_text.py mockup.html

Renders the page in headless Chrome (so text drawn by scripts is included),
then prints each distinct visible string, numbered, with a word count.
Falls back to the static HTML if Chrome isn't found.
"""
import html
import os
import re
import shutil
import subprocess
import sys

CHROME_PATHS = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    shutil.which("google-chrome") or "",
    shutil.which("chromium") or "",
]


def render(path):
    chrome = next((p for p in CHROME_PATHS if p and os.path.exists(p)), None)
    if chrome:
        out = subprocess.run(
            [chrome, "--headless=new", "--disable-gpu", "--virtual-time-budget=3000",
             "--dump-dom", "file://" + os.path.abspath(path)],
            capture_output=True, text=True, timeout=60)
        if out.stdout.strip():
            return out.stdout, True
    return open(path, encoding="utf-8").read(), False


def strings(dom):
    dom = re.sub(r"(?s)<(script|style|head|title)[^>]*>.*?</\1>", " ", dom)
    dom = re.sub(r"(?s)<!--.*?-->", " ", dom)
    dom = re.sub(r"<(br|/p|/div|/h\d|/li|/text|/tspan|/span|/button|/td|/th|/label|/a|/strong|/em)[^>]*>", "\n", dom)
    text = html.unescape(re.sub(r"<[^>]+>", " ", dom))
    seen = []
    for line in text.split("\n"):
        line = re.sub(r"\s+", " ", line).strip()
        if line and line not in seen:
            seen.append(line)
    return seen


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    dom, rendered = render(sys.argv[1])
    lines = strings(dom)
    total = sum(len(l.split()) for l in lines)
    print(f"{len(lines)} distinct strings, {total} words ({'rendered' if rendered else 'static HTML only'})\n")
    for i, line in enumerate(lines, 1):
        print(f"{i:3d}  {line}")


if __name__ == "__main__":
    main()
