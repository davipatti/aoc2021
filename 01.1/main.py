#!/usr/bin/env python3

import sys
import math

increases = 0
previous = math.inf
for line in sys.stdin:
    current = int(line)
    if current > previous:
        increases += 1
    previous = current
print(increases)
