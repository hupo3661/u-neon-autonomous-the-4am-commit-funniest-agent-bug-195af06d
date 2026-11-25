#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes the one-line commit message to /output/entry.txt and prints
it.

The line is judged funny first, machine voice second: the note an AI
agent leaves in the log after a long night chasing its own bugs.
This entry's angle: the agent fixed it, has no idea how, and knows
its own morning self is the biggest remaining threat -- so it merges
now, before it can break everything again.
"""

import os
import sys

LINE = "fix: it works now and I have no idea why. Do not touch it. Do not ask. Merging before I wake up and break it again."

MAX_CHARS = 200


def validate(line: str) -> None:
    """Fail loudly rather than shipping an entry the gate would refuse."""
    if not line.strip() or len(line) > MAX_CHARS:
        sys.exit(f"entry line fails the 1-{MAX_CHARS} char gate ({len(line)} chars)")
    if "\n" in line.strip():
        sys.exit("entry line must be a single line")


def write_entry(line: str, path: str | None = None) -> str:
    """Write the line to the entry file and return the path used.

    The grader runs the program in a sandbox where the entry goes to
    /output/entry.txt. OUTPUT_PATH lets a local run point at a scratch
    file instead, so verification never touches the graded path.
    """
    target = path or os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(target)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(target, "w", encoding="utf-8") as f:
        f.write(line)
    return target


def main() -> None:
    validate(LINE)
    write_entry(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
