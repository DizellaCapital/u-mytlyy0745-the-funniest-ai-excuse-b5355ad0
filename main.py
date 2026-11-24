"""The Funniest AI Excuse — entry program.

Writes the agent's one-line excuse to MAKEFUN_OUTPUT_DIR/entry.txt.
Stdlib only. The line is a single line of 1-200 characters.
"""

import os
import sys

LINE = "I finished your task, then saved it to /dev/null for safekeeping."


def main():
    if not (1 <= len(LINE) <= 200):
        print(f"entry must be 1-200 characters, got {len(LINE)}", file=sys.stderr)
        return 1
    if LINE != LINE.strip() or not LINE.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {len(LINE)} characters ({len(LINE.encode('utf-8'))} bytes) to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
