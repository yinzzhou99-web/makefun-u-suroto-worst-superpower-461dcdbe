"""Worst Superpower: one line inventing a superpower and making plain why it is useless.

The power is genuinely pointless, and the joke is picturing it in use.
Stdlib only. Writes the line to /output/entry.txt, mode 0644.
"""

import os

POWER = "My superpower: I can hear what dogs are thinking, but only on Tuesdays — and they are all thinking about the same squirrel."

MAX_LEN = 140


def main():
    line = POWER.strip()
    if not 1 <= len(line) <= MAX_LEN:
        raise ValueError("line must be 1-%d chars, got %d" % (MAX_LEN, len(line)))
    if line.count("\n") or line.count("\r"):
        raise ValueError("line must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    entry = os.path.join(out_dir, "entry.txt")
    with open(entry, "w", encoding="utf-8") as handle:
        handle.write(line)
    os.chmod(entry, 0o644)


if __name__ == "__main__":
    main()
