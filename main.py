#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun entry.

Writes the entry line to /output/entry.txt, reads it back,
and asserts it is exactly one line of 1-120 characters.
"""

import os

# The entry: a deadpan apology from a toaster that has failed
# at the one job it has. The joke is the contrast between the
# polite, remorseful tone ("I'm sorry", "I gave it my best")
# and the confession that follows: its best effort was simply
# setting the bread on fire. No setup, no second sentence
# needed — the punchline is the last word.
ENTRY = "I'm sorry — your toast is now charcoal. I gave it my best, and my best was fire."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

    with open(OUTPUT_PATH, encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines()
    assert len(lines) == 1, f"expected exactly 1 line, got {len(lines)}"
    line = lines[0]
    assert line.strip(), "entry must not be only whitespace"
    assert 1 <= len(line) <= 120, f"entry is {len(line)} chars, must be 1-120"
    print(f"OK: {len(line)} chars, 1 line")
    print(line)


if __name__ == "__main__":
    main()
