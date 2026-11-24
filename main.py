"""Loading Screen Gold entry: write one loading-screen tip to /output/entry.txt.

The tip is a single line of at most 200 characters, aimed at stressed
developers and AI coding agents. It is written as a literal string in this
file so the program's output is fully deterministic: no network, no random
input, no file outside this repository is read.
"""

import os
import sys

MAX_CHARS = 200

TIP = (
    "Tip: if this screen outlasts your patience, blame the prompt, "
    "not the agent \u2014 it only did exactly what you said."
)


def main() -> int:
    line = TIP
    if not line or not line.strip():
        print("entry must not be empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(f"entry is {len(line)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
