import sys
import heapq
from collections import Counter


def main(filename):
    coords = []
    with open(filename, "r") as fp:
        for line in fp:
            x, y = map(int, line.split(","))
            coords.append((x, y))

    max_x = max(p[0] for p in coords)
    min_x = min(p[0] for p in coords)
    min_y = min(p[0] for p in coords)
    max_y = max(p[1] for p in coords)

    top_left = (min_x, min_y)
    bottom_right = (max_x, max_y)
    print("top left", top_left)
    print("bottom right", bottom_right)
    infinite = set()
    areas = Counter()
    part2_area = 0
    for x in range(top_left[0], bottom_right[0] + 1):
        for y in range(top_left[1], bottom_right[1] + 1):
            idx, heap = find_closest_index(x, y, coords)
            distance_to_all = sum([x[0] for x in heap])
            if distance_to_all < 10000:
                part2_area += 1

            if idx:
                if (
                    x == top_left[0]
                    or x == bottom_right[0]
                    or y == top_left[1]
                    or y == bottom_right[1]
                ):
                    infinite.add(idx)
                areas[idx] += 1

    best_non_infinite = [
        (idx, area) for (idx, area) in areas.most_common() if idx not in infinite
    ]

    print("part1", best_non_infinite)
    print("part2", part2_area)


def find_closest_index(x, y, coords):
    heap = []
    for index, coord in enumerate(coords):
        distance = abs(x - coord[0]) + abs(y - coord[1])
        heapq.heappush(heap, (distance, index))
    d1, closest_idx = heap[0]
    d2, next_idx = heap[1]
    if d1 == d2:
        return None, heap
    return closest_idx, heap


if __name__ == "__main__":
    main(sys.argv[1])
