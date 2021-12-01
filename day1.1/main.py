#!/usr/bin/env python3
import sys

increases = 0
previous = None
for line in sys.stdin:
    if previous is not None:
        current = int(line.strip())
        if current > previous:
            increases += 1
        previous = current
    else:
        previous = int(line.strip())
print(increases)
