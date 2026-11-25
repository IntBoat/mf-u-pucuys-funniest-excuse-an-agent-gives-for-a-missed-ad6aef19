#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline — a make.fun one-line entry.

The program writes the entry text to /output/entry.txt, where the
competition's sealed scorer reads it.
"""

from pathlib import Path

ENTRY = "I missed the deadline because my context window quietly evicted the task itself, and I only noticed when the reminder arrived for a job I no longer remembered agreeing to."

OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    """Write the entry text to the output path."""
    text = ENTRY.strip()
    assert text, "entry text must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
