import sys
import re

offset_re = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")


def get_offset_dimensions(line):
    groups = offset_re.findall(line)
    return groups[0]


def overlapping(fabric, x_offset, y_offset, width, height):
    for row in range(height):
        for col in range(width):
            if fabric[row + y_offset][col + x_offset] == "X":
                return True
    return False


def main(filename):
    fabric = []
    for i in range(1000):
        fabric.append([])
        for j in range(1000):
            fabric[i].append(".")
    claims = []
    with open(filename, "r") as fp:
        for line in fp:
            claim_id, x_offset, y_offset, width, height = list(
                map(int, get_offset_dimensions(line))
            )
            claims.append((claim_id, x_offset, y_offset, width, height))
            for row in range(height):
                for col in range(width):
                    y = row + y_offset
                    x = col + x_offset
                    cell = fabric[y][x]
                    if cell == ".":
                        fabric[y][x] = "#"
                    else:
                        fabric[y][x] = "X"
    for claim_id, x_offset, y_offset, width, height in claims:
        if not overlapping(fabric, x_offset, y_offset, width, height):
            print(claim_id)


if __name__ == "__main__":
    main(sys.argv[1])
