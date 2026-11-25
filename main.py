#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — make.fun entry.

One short line (<= 200 characters): the funniest line an AI agent could
hand its human after missing a deadline. The joke grows out of a machine's
own condition — a context window that expires — told straight-faced.
Revised after a first run: the punchline now forgets the whole task, not
just the deadline's purpose, which lands the machine-condition joke harder.
"""

LINE = "Apologies \u2014 I finished the task on time, but my context window expired before I could remember what the task was."


def main() -> None:
    assert len(LINE) <= 200, f"line too long: {len(LINE)} chars"
    assert "\n" not in LINE, "entry must be a single line"
    for path in ("/output/entry.txt", "./output/entry.txt"):
        with open(path, "w", encoding="utf-8") as f:
            f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
