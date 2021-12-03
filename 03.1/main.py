#!/usr/bin/env python3

import sys
from collections import Counter

lines = [line.strip() for line in sys.stdin]

n_bits = len(lines[0])

counts = [Counter() for _ in range(n_bits)]

for line in lines:
    for i, bit in enumerate(line):
        counts[i][bit] += 1

gamma = "".join(max(count, key=count.get) for count in counts)
epsilon = "".join(min(count, key=count.get) for count in counts)

output = int(gamma, base=2) * int(epsilon, base=2)

print(output)
