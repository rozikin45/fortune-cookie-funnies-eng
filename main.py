#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers — make.fun entry.

Writes one original fortune-cookie line for a software engineer to
/output/entry.txt. The line is fixed text (no randomness, no network, no
input files), so every run produces byte-identical output.
"""

from pathlib import Path

# One original fortune-cookie line, 98 characters (gate: 1-120).
LINE = (
    "Your pull request will be approved instantly "
    "\u2014 by the bot you wrote to approve your pull requests."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Self-check against the competition gate: UTF-8 text, 1-120 chars,
    # not only white space. Fail loudly instead of writing an invalid line.
    stripped = LINE.strip()
    assert 1 <= len(LINE) <= 120, f"line is {len(LINE)} chars, gate is 1-120"
    assert stripped, "line must not be only white space"
    assert "\n" not in LINE, "entry must be a single line"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
