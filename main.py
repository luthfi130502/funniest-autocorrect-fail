#!/usr/bin/env python3
"""Writes one autocorrect-fail line to /output/entry.txt."""

import os

LINE = "Come home soon, the cake is in the coven and the candles are already lit."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 199 characters.
    assert 1 <= len(LINE) <= 199, "entry line outside the 1-199 char gate"
    assert LINE.strip(), "entry line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
