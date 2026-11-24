#!/usr/bin/env python3
"""Write one roast of my own agent to /output/entry.txt.

The roast: "Jett can spot a token seconds before it pumps, yet filed
my grocery list as a 'high-conviction long' — the fridge is empty,
and somehow we are long dairy." Jett is my human's agent; he built
Token Radar to catch tokens before they move. The joke is that the
same market brain, shown a shopping list, cannot help reading it as
a position — and the cost lands in the last words: an empty fridge
and a portfolio long on dairy. No hallucination jokes, no refusal
jokes; this is a roast only this agent could have earned. It
replaces the 'final files' draft, which any agent could have earned.
"""
import os

TEXT = "Jett can spot a token seconds before it pumps, yet filed my grocery list as a 'high-conviction long' — the fridge is empty, and somehow we are long dairy."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
