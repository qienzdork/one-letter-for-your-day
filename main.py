"""One Letter for Your Day — entry program.

Writes a single letter, "X", to /output/entry.txt (or $OUTPUT_PATH).

The letter stands for "exhausted": the day crossed you out. X is the
mark of a day that is over, done, cancelled — a vivid, funny, honest
report of a day that ran you flat, and the sharpest initial for it:
E would be the obvious pick for "exhausted"; X is the shape of being
crossed out.
"""

import os

LETTER = "X"
DEFAULT_OUTPUT = "/output/entry.txt"


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH") or DEFAULT_OUTPUT
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    # Exactly one character, no trailing newline: the gate is 1 to 1
    # characters, and a newline would make it 2 bytes.
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LETTER)


if __name__ == "__main__":
    main()

# Notes on the entry, kept with the program:
# - Deterministic: no randomness, no network, stdlib only; every run
#   writes the same single byte, "X".
# - The gate counts characters, so the file must hold exactly one
#   character and no newline. A trailing newline would be a second
#   character and fail the gate.
# - "X" was chosen over the rules' own examples (A amazing, F
#   Friday-feeling, Z zero sleep) precisely because those examples
#   will be the most common letters in the field; X for "exhausted"
#   is vivid, funny, true, and its shape — crossed out — fits the word
#   better than the obvious initial E.
