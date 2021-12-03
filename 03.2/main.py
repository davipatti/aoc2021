#!/usr/bin/env python3

import sys
from collections import Counter


def keep(numbers, i, which):
    """Keep numbers with the least or most common bit at index i."""
    counts = Counter(number[i] for number in numbers)

    if which == "most_common":
        value = "0" if counts["0"] > counts["1"] else "1"
    elif which == "least_common":
        value = "1" if counts["1"] < counts["0"] else "0"
    else:
        raise ValueError(which)

    return [n for n in numbers if n[i] == value]


def filter_numbers(numbers, which):
    """
    Iterate through bits in numbers, keeping only numbers that have the least or
    most common bit at each bit.
    """
    i = 0
    while len(numbers) > 1:
        numbers = keep(numbers, i, which)
        i += 1
    return numbers


numbers = tuple(line.strip() for line in sys.stdin)

o2_gen = filter_numbers(numbers, "most_common")
co2_scrub = filter_numbers(numbers, "least_common")

output = int(o2_gen[0], 2) * int(co2_scrub[0], 2)

print(output)
