#!/usr/bin/python3
"""
markdown script
"""
import sys
import os


def markdown2html():
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md"
              " README.html", file=sys.stderr)
        sys.exit(1)
    if not os.path.isfile(sys.argv[1]):
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        exit(1)
    exit(0)


if __name__ == "__main__":
    markdown2html()
