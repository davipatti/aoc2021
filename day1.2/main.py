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
triplets = chunks(numbers, 3)
increases = sum(sum(b) > sum(a) for a, b in chunks(triplets, 2))
print(increases)
