#!/usr/bin/env python3

import sys
from collections import Counter


def timestep(counts):
    zeros = counts.pop(0, None)
    new = Counter({state - 1: count for state, count in counts.items()})
    if zeros:
        new[6] += zeros
        new[8] += zeros
    return new


def timesteps(counts, n):
    for _ in range(n):
        counts = timestep(counts)
    return counts


def sum_after_n_days(initial, n):
    return sum(timesteps(initial, n).values())


if __name__ == "__main__":
    counts = Counter([int(n) for n in next(sys.stdin).split(",")])
    print(sum_after_n_days(counts, 80))
    print(sum_after_n_days(counts, 256))
