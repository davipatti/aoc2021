#!/usr/bin/env python3

import sys
from itertools import product


class Grid:
    def __init__(self, lines):
        self.grid = [[int(char) for char in line.strip()] for line in lines]
        self.height = len(self.grid)
        self.width = len(self.grid[0])

    def __iter__(self):
        for i, j in product(range(self.height), range(self.width)):
            yield (i, j), self[(i, j)]

    def __getitem__(self, ij):
        i, j = ij
        return self.grid[i][j]

    def adjacent(self, ij):
        i, j = ij
        if i > 0:
            yield i - 1, j
        if i < (self.height - 1):
            yield i + 1, j
        if j > 0:
            yield i, j - 1
        if j < (self.width - 1):
            yield i, j + 1

    def risk_lowpoints(self):
        total = 0
        for ij, value in self:
            if all(self[adjacent] > value for adjacent in self.adjacent(ij)):
                total += value + 1
        return total

    def grow_basin(self, from_, existing):
        existing = set() if existing is None else existing
        existing.add(from_)
        for point in grid.adjacent(from_):
            if point not in existing and self[point] != 9:
                existing = self.grow_basin(point, existing)
        return existing

    def find_basins(self):
        basins = []
        for ij, value in self:
            if not (value == 9 or any(ij in basin for basin in basins)):
                basins.append(self.grow_basin(from_=ij, existing=None))
        return basins

    def product_largest_three_basins(self):
        basin_sizes = sorted(len(basin) for basin in self.find_basins())
        return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]


if __name__ == "__main__":
    grid = Grid(sys.stdin.readlines())
    print(grid.risk_lowpoints())  # Part 1
    print(grid.product_largest_three_basins())  # Part 2
