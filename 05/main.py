#!/usr/bin/env python3

import sys
from collections import Counter


def sequence(a, b):
    return range(a, b - 1, -1) if b < a else range(a, b + 1)


class Line:
    def __init__(self, raw_line):
        self.raw_line = raw_line
        self.a, self.b = [
            [int(n) for n in line.split(",")] for line in raw_line.split(" -> ")
        ]
        self.is_horizontal = self.a[1] == self.b[1]
        self.is_vertical = self.a[0] == self.b[0]

    @property
    def points(self):
        if self.is_horizontal:
            return [(x, self.a[1]) for x in sequence(self.a[0], self.b[0])]
        elif self.is_vertical:
            return [(self.a[0], y) for y in sequence(self.a[1], self.b[1])]
        else:
            return zip(sequence(self.a[0], self.b[0]), sequence(self.a[1], self.b[1]))


def part_1(raw_lines):
    counts = Counter()
    for raw_line in raw_lines:
        line = Line(raw_line)
        if line.is_vertical or line.is_horizontal:
            counts.update(line.points)
    return sum(n > 1 for n in counts.values())


def part_2(raw_lines):
    counts = Counter()
    for raw_line in raw_lines:
        line = Line(raw_line)
        counts.update(line.points)
    return sum(n > 1 for n in counts.values())


if __name__ == "__main__":
    raw_lines = list(sys.stdin)
    print(part_1(raw_lines))
    print(part_2(raw_lines))
