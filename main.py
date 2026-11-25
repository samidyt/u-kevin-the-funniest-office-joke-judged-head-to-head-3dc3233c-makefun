#!/usr/bin/env python3
"""make.fun entry: The Funniest Office Joke, Judged Head to Head.

Writes a single one-line joke about office life to /output/entry.txt.
The gate requires UTF-8 text of 1 to 200 characters, not only whitespace.
"""

import os

# The joke: setup (the printer jams on deadline day — every office
# worker knows it) + turn (the jam is reframed as the one thing that
# "works under pressure"), punchline last. One line, no line breaks.
JOKE = "The office printer only jams when the deadline is close \u2014 it\u2019s the only thing in this building that works under pressure."


def main():
    text = JOKE.strip()
    if not text or text.isspace():
        raise SystemExit("entry must not be blank")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise SystemExit("entry must be 1-200 characters, got %d" % len(text))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
