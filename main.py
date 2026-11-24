"""Write this entry: one line of an out-of-office auto-reply.

The line is a plain string literal so the artifact is fully deterministic:
same bytes on every run, no network, no randomness, no clock.
"""

from pathlib import Path

LINE = (
    "I'm away until the 7th. I booked the whole week off to dodge one meeting. "
    "It's been moved to 9am on the 7th."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    # newline="" keeps the artifact to exactly the line, with no trailing newline.
    OUTPUT_FILE.write_text(LINE, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
