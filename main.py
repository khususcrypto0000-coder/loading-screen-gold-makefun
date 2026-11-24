#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes one loading-screen tip (1-200 characters, single line) to
/output/entry.txt (or $OUTPUT_DIR/entry.txt).
Stdlib only.
"""

import os
import sys

ENTRY_TEXT = (
    "Loading\u2026 Go touch grass while this finishes. "
    "The bug that's mocked you for two hours is terrified "
    "of a rested brain \u2014 go scare it."
)
# Angle: "touch grass" — zero collisions with the 860 scanned
# submission titles for this bounty (bug/tests/commit/breathe/
# stretch/blame/spinner/stuck/rewrote/diff/water are saturated).


def main():
    text = ENTRY_TEXT
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be whitespace only"
    assert "\n" not in text and "\r" not in text, "entry must be one line"

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = text.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    # Read-back: byte-identical, no trailing newline.
    with open(path, "rb") as f:
        back = f.read()
    assert back == data, "read-back mismatch"
    assert not back.endswith(b"\n"), "trailing newline found"
    print("Wrote %s (%d chars, %d bytes)" % (path, len(text), len(data)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
