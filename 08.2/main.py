#!/usr/bin/env python3

import sys
from itertools import permutations

table = dict(zip("abcdefg", range(7)))


def translate(letters):
    return [table[l] for l in letters]


def wire(wiring, pattern):
    return frozenset(wiring[p] for p in pattern)


digits = (
    (0, 1, 2, 4, 5, 6),  # 0
    (2, 5),  # 1,
    (0, 2, 3, 4, 6),  # 2,
    (0, 2, 3, 5, 6),  # 3,
    (1, 2, 3, 5),  # 4,
    (0, 1, 3, 5, 6),  # 5,
    (0, 1, 3, 4, 5, 6),  # 6,
    (0, 2, 5),  # 7,
    (0, 1, 2, 3, 4, 5, 6),  # 8,
    (0, 1, 2, 3, 5, 6),  # 9,
)

allowed = set(map(frozenset, digits))


class SevenSegmentDisplay:
    def __init__(self, patterns):
        self.patterns = [translate(pattern) for pattern in patterns]

        for wiring in permutations(range(7), 7):

            for pattern in self.patterns:
                wiring_consistent = wire(wiring, pattern) in allowed

                if not wiring_consistent:
                    break

            else:
                self.wiring = wiring
                break

    def display(self, pattern):
        segments = wire(self.wiring, translate(pattern))
        return digits.index(tuple(sorted(segments)))

    def display_multiple(self, patterns):
        digits = [str(self.display(pattern)) for pattern in patterns]
        return int("".join(digits))


if __name__ == "__main__":
    n = 0
    for line in sys.stdin:
        patterns, outputs = line.strip().split(" | ")
        ssd = SevenSegmentDisplay(patterns.split())
        n += ssd.display_multiple(outputs.split())

    print(n)
