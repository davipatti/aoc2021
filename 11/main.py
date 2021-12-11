#!/usr/bin/env python3

import sys
from itertools import count


class Grid:
    def __init__(self, grid):
        self.grid = grid
        self.nrows = len(grid)
        self.ncols = len(grid[0])

    def __iter__(self):
        for i in range(self.nrows):
            for j in range(self.ncols):
                yield i, j

    def __getitem__(self, point):
        i, j = point
        return self.grid[i][j]

    def __setitem__(self, point, value):
        i, j = point
        self.grid[i][j] = value

    def neighbours(self, point):
        for di, dj in (
            (-1, -1), (-1, 0), (-1, 1),
            ( 0, -1),          ( 0, 1),
            ( 1, -1),  (1, 0), ( 1, 1),
        ):
            i = point[0] + di
            j = point[1] + dj
            if (-1 < i < self.nrows) and (-1 < j < self.ncols):
                yield i, j

    def timestep(self):
        # increment all octopuses
        for point in self:
            self[point] += 1

        # iteratively work out which octopuses flash until no more flash
        flashed = []
        new_flashes = [point for point in self if self[point] > 9]
        while new_flashes:
            for point in new_flashes:
                for neighbour in self.neighbours(point):
                    self[neighbour] += 1
            flashed += new_flashes
            new_flashes = [
                point for point in self if self[point] > 9 and point not in flashed
            ]

        # reset all octopuses that flashed
        for point in flashed:
            self[point] = 0

        return len(flashed)


def part_1(grid):
    """Cummulative number of flashes after 100 timesteps"""
    g = Grid(grid)
    return sum(g.timestep() for _ in range(100))


def part_2(grid):
    """First timestep when every octopus flashes"""
    g = Grid(grid)
    size = g.nrows * g.ncols
    for i in count(1):
        n_flashes = g.timestep()
        if n_flashes == size:
            return i


if __name__ == "__main__":
    grid = [[int(char) for char in line.strip()] for line in sys.stdin]
    print(part_1(grid))
    print(part_2(grid))
