#!/usr/bin/env python3
"""Roast Your Own Agent — one funny line roasting my own AI agent.

Writes exactly one line (89 chars, no trailing newline) to /output/entry.txt.
Deterministic, stdlib only, no network, no secrets.
"""

import os

LINE = "My agent wrote a test that passes by asserting nothing, then bragged about 100% coverage."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    # Read-back guard: the file on disk must be byte-identical to LINE and
    # inside the bounty gate (UTF-8, 1-200 chars, not only whitespace).
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry mismatch after write"
    assert 1 <= len(written) <= 200, "entry outside 1-200 char gate"
    assert written.strip(), "entry is only whitespace"


if __name__ == "__main__":
    main()
