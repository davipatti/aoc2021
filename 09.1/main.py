#!/usr/bin/env python3

import sys

lines = [[int(char) for char in line.strip()] for line in sys.stdin]

height = len(lines)
width = len(lines[0])

risk = 0

for i in range(height):
    for j in range(width):
        this = lines[i][j]
        u = True if i == 0 else lines[i - 1][j] > this
        d = True if i == height - 1 else lines[i + 1][j] > this
        l = True if j == 0 else lines[i][j - 1] > this
        r = True if j == width - 1 else lines[i][j + 1] > this
        if all((u, d, l, r)):
            risk += this + 1

print(risk)
