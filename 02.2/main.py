#!/usr/bin/env python3

import sys

aim = 0
x = 0  # Horizontal displacement
y = 0  # Vertical displacement

for line in sys.stdin:
    direction, value = line.strip().split()
    value = int(value)

    if direction == "down":
        aim += value
    elif direction == "up":
        aim -= value
    elif direction == "forward":
        x += value
        y += aim * value
    else:
        raise ValueError("Unknown direction: {}" % direction)


print(x * y)
