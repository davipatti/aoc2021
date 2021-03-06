#!/usr/bin/env python3

import sys
from functools import lru_cache


@lru_cache
def move_cost(x):
    """Cost of moving a single crab x positions"""
    return sum(range(x))


def fuel_cost(i, positions):
    """Cost of moving all crabs to position i"""
    return sum(move_cost(abs(position - i)) for position in positions)


if __name__ == "__main__":
    positions = [int(n) for n in next(sys.stdin).split(",")]
    x = range(min(positions), max(positions) + 1)
    print(min(fuel_cost(i, positions) for i in x))
