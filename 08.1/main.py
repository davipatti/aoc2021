#!/usr/bin/env python3

import sys

unique_segments = {
    2,  # 1
    4,  # 4
    3,  # 7
    7,  # 8
}

n = 0
for line in sys.stdin:
    _, output = line.strip().split(" | ")
    n += sum(len(digit) in unique_segments for digit in output.split())

print(n)
