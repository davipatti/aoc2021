#!/usr/bin/env python3

import math
import sys


def chunks(iterable, n):
    """Generate size n chunks of something."""
    items = tuple(iterable)
    i = 0
    j = n
    while j <= len(items):
        yield items[i:j]
        i += 1
        j += 1

numbers = [int(line.strip()) for line in sys.stdin]

increases = 0
previous = math.inf  # First chunk cannot be an increase, so compare to infinity
for chunk in chunks(numbers, 3):
    current = sum(chunk)
    if current > previous:
        increases += 1
    previous = current

print(increases)
