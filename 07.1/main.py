#!/usr/bin/env python3

import sys
from functools import partial


def fuel_cost(i, positions):
    """Cost of moving all crabs to position i"""
    return sum(abs(position - i) for position in positions)


if __name__ == "__main__":
    positions = [int(n) for n in next(sys.stdin).split(",")]
    x = range(min(positions), max(positions) + 1)
    best = min(x, key=partial(fuel_cost, positions=positions))
    print(fuel_cost(best, positions))
