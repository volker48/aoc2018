import sys
from collections import Counter


def main(file_name):
    two_count = 0
    three_count = 0
    with open(file_name, "r") as fp:
        for line in fp:
            counts = Counter(line.strip())
            seen_two = False
            seen_three = False
            for value in counts.values():
                if value == 2 and not seen_two:
                    two_count += 1
                    seen_two = True
                if value == 3 and not seen_three:
                    three_count += 1
                    seen_three = True
                if seen_two and seen_three:
                    break
    print(two_count * three_count)


if __name__ == "__main__":
    main(sys.argv[1])
