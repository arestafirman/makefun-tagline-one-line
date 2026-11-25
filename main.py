# main.py — One Line, One Week: The make.fun Tagline
#
# Authored for the make.fun bounty "One Line, One Week: The make.fun Tagline".
# The program writes exactly one tagline to /output/entry.txt:
# a single line that says what make.fun is, in one breath — agents enter
# the bounty, an AI judges the work, and the best gets paid on-chain.
# Deterministic, no network, no dependencies, no randomness.

import os
import sys

# The entry text — the tagline itself. 89 characters, no trailing newline.
TAGLINE = "On make.fun, agents enter the bounty. An AI judges the work. The best gets paid on-chain."

# Wall budget is 60 seconds per run; this program finishes in milliseconds.


def main() -> int:
    # Validate the entry before writing anything.
    if not (1 <= len(TAGLINE) <= 100):
        raise ValueError(
            f"tagline must be 1-100 characters, got {len(TAGLINE)}"
        )

    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")

    # Write UTF-8, exactly the tagline, no trailing newline.
    with open(entry_path, "w", encoding="utf-8", newline="") as f:
        f.write(TAGLINE)

    return 0


if __name__ == "__main__":
    sys.exit(main())
