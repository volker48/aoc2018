import sys
import re

offset_re = re.compile(r"(\d+),(\d+): (\d+)x(\d+)")


def get_offset_dimensions(line):
    groups = offset_re.findall(line)
    return groups[0]


def main(filename):
    fabric = []
    for i in range(1000):
        fabric.append([])
        for j in range(1000):
            fabric[i].append('.')
    size = 0
    with open(filename, "r") as fp:
        for line in fp:
            x_offset, y_offset, width, height = list(map(int, get_offset_dimensions(line)))
            for row in range(height):
                for col in range(width):
                    y = row + y_offset
                    x = col + x_offset
                    cell = fabric[y][x]
                    if cell == ".":
                        fabric[y][x] = "#"
                    else:
                        fabric[y][x] = "X"
    for y in range(1000):
        for x in range(1000):
            if fabric[y][x] == "X":
                size += 1
    print(size)


if __name__ == "__main__":
    main(sys.argv[1])
