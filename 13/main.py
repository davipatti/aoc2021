#!/usr/bin/env python3

import re
import sys


def parse_lines(lines):
    folds = []
    points = set()
    for line in lines:
        match = re.match(r"fold along ([yx])=(\d+)", line)
        if match:
            dim, loc = match.groups()
            folds.append((dim, int(loc)))
        elif line:
            points.add(tuple(map(int, line.strip().split(","))))
    return folds, points


def fold(points, dim, loc):
    dim = {"x": 0, "y": 1}[dim]
    new_points = set()
    for pt in points:
        new = list(pt)
        new[dim] = pt[dim] if pt[dim] < loc else loc - (pt[dim] - loc)
        new_points.add(tuple(new))
    return new_points


def render(points):
    x = [pt[0] for pt in points]
    y = [pt[1] for pt in points]
    output = ""
    for j in range(max(y) + 1):
        for i in range(max(x) + 1):
            output += "x" if (i, j) in points else " "
        output += "\n"
    return output


def part_1(folds, points):
    points = fold(points, folds[0][0], folds[0][1])
    return len(points)


def part_2(folds, points):
    for f in folds:
        points = fold(points, f[0], f[1])
    return render(points)


if __name__ == "__main__":
    folds, points = parse_lines([line.strip() for line in sys.stdin])
    print(part_1(folds, points))
    print(part_2(folds, points))
