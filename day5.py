import sys
import string
import re


def has_reaction(c1, c2):
    return abs(ord(c1) - ord(c2)) == 32


def collapse(polymers):
    pos = 0
    while pos < len(polymers) - 1:
        if has_reaction(*polymers[pos : pos + 2]):
            polymers = polymers[:pos] + polymers[pos + 2 :]
            pos = max(0, pos - 1)
        else:
            pos += 1
    return len(polymers)


def main(filename):
    with open(filename, "r") as fp:
        polymers = fp.read()
    length = collapse(polymers)
    print("part1", length)

    shortest = length
    for char in string.ascii_lowercase:
        removed = re.sub(rf"[{char}{char.upper()}]", "", polymers)
        shortest = min(shortest, collapse(removed))
    print("part2", shortest)


if __name__ == "__main__":
    main(sys.argv[1])
