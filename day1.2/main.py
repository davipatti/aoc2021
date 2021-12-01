#!/usr/bin/env python3

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

numbers = (int(line) for line in sys.stdin)
triplet_sums = (sum(triplet) for triplet in chunks(numbers, 3))
increases = sum(b > a for a, b in chunks(triplet_sums, 2))
print(increases)
