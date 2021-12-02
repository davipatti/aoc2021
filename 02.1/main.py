#!/usr/bin/env python3

import sys
from collections import defaultdict

totals = defaultdict(int)
for line in sys.stdin:
    direction, distance = line.strip().split()
    totals[direction] += int(distance)

output = (totals["down"] - totals["up"]) * totals["forward"]

print(output)
