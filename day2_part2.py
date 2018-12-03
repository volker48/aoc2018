import sys


def hamming(s1, s2):
    distance = 0
    positions = []
    for position, (c1, c2) in enumerate(zip(s1, s2)):
        if c1 != c2:
            distance += 1
            positions.append(position)
    return positions, distance


def main(file_name):
    with open(file_name, "r") as fp:
        ids = fp.readlines()
    for i in range(len(ids) - 1):
        for j in range(i + 1, len(ids)):
            positions, distance = hamming(ids[i], ids[j])
            if distance == 1:
                s = ids[i]
                position = positions[0]
                print(s[:position] + s[position + 1 :])


if __name__ == "__main__":
    main(sys.argv[1])
