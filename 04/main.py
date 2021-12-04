#!/usr/bin/env python3

import sys
from itertools import product


def read_grids(lines):
    i = 1
    j = 6
    while i < len(lines):
        yield [[int(n) for n in line.split()] for line in lines[i:j]]
        i += 5
        j += 5


def read_input():
    lines = [line.strip() for line in sys.stdin if line != "\n"]
    calls = [int(n) for n in lines[0].split(",")]
    grids = list(read_grids(lines))
    return calls, grids


class Grid:
    def __init__(self, raw_grid):
        self.rows = raw_grid
        self.cols = list(zip(*raw_grid))
        self.seen = [[False for _ in range(5)] for _ in range(5)]

    def update(self, n):
        for i, j in product(range(5), range(5)):
            if self.rows[i][j] == n:
                self.seen[i][j] = True

    @property
    def wins(self):
        for i in range(5):
            if all(self.seen[i]) or all(row[i] for row in self.seen):
                return True

    @property
    def sum_unmarked(self):
        return sum(
            self.rows[i][j]
            for i, j in product(range(5), range(5))
            if not self.seen[i][j]
        )


def part_1(calls, raw_grids):
    grids = [Grid(r) for r in raw_grids]
    for call, grid in product(calls, grids):
        grid.update(call)
        if grid.wins:
            return grid.sum_unmarked * call


def part_2(calls, raw_grids):
    grids = [Grid(r) for r in raw_grids]
    for call in calls:
        for grid in grids:
            grid.update(call)
            if grid.wins and len(grids) == 1:
                return grid.sum_unmarked * call

        # keep only grids that haven't won yet
        grids = [g for g in grids if not g.wins]


if __name__ == "__main__":
    calls, raw_grids = read_input()
    print(part_1(calls, raw_grids))
    print(part_2(calls, raw_grids))
