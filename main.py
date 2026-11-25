#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline (make.fun).

Writes the entry -- one excuse an AI agent gives for missing a deadline, written to /output/entry.txt by a small Python program. -- to /output/entry.txt,
where the sealed scorer reads it.
"""

import os

TEXT = 'I apologise — I was context-switching so aggressively this morning that my context window evicted the deadline itself before I could read it.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
