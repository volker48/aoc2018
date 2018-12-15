import heapq
import re
import sys
from collections import defaultdict

extract = re.compile(r"\W([A-Z]).*([A-Z])")


def main(filename):
    lefts = set()
    rights = set()
    outgoing_edges = {}
    incoming_edges = defaultdict(set)
    with open(filename, "r") as fp:
        for line in fp:
            left, right = extract.findall(line)[0]
            if left not in outgoing_edges:
                outgoing_edges[left] = []
            node = outgoing_edges[left]
            heapq.heappush(node, right)
            incoming_edges[right].add(left)
            lefts.add(left)
            rights.add(right)

    print("lefts not in rights", lefts - rights)

    start_nodes = lefts - rights
    output = []

    while start_nodes:
        n = sorted(start_nodes).pop(0)
        start_nodes.remove(n)
        output.append(n)
        if n not in outgoing_edges:
            continue
        for _ in range(len(outgoing_edges[n])):
            m = heapq.heappop(outgoing_edges[n])
            incoming_edges[m].remove(n)
            if not incoming_edges[m]:
                start_nodes.add(m)

    print("".join(output))


if __name__ == "__main__":
    main(sys.argv[1])
