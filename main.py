"""One-line office joke entry for make.fun's
"One-Line Office Joke: 24-Hour Sprint" bounty.

Writes a single original office joke to the output path.
Deterministic, standard library only, no network access,
reads nothing outside this repo.
"""

import os

JOKE = (
    "Our office suggestion box gets exactly one note a month, "
    "and it always reads: 'Please remove this box.'"
)

OUTPUT_PATH = os.environ.get("JOKE_OUTPUT", "/output/entry.txt")


def main() -> None:
    output_dir = os.path.dirname(OUTPUT_PATH)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
