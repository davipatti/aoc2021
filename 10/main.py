#!/usr/bin/env python3

import sys
from functools import reduce


pairs = {"(": ")", "{": "}", "<": ">", "[": "]"}


def invalid(line):
    """First invalid character in a line"""
    stack = []
    for char in line:
        if char in pairs:
            stack.append(char)
        elif char != pairs[stack.pop()]:
            return char


def complete(line):
    """Complete a line"""
    stack = []
    for char in line:
        if char in pairs:
            stack.append(char)
        else:
            stack.pop()
    completion = ""
    while stack:
        completion += pairs[stack.pop()]
    return completion


def score(completion):
    """Score of a completion string"""
    scores = {")": 1, "]": 2, "}": 3, ">": 4}
    return reduce(lambda a, b: a * 5 + scores[b], completion, 0)


def part_1(lines):
    scores = {")": 3, "}": 1197, ">": 25137, "]": 57}
    n = 0
    for line in lines:
        char = invalid(line)
        if char:
            n += scores[char]
    return n


def part_2(lines):
    scores = sorted(score(complete(line)) for line in lines if not invalid(line))
    return scores[(len(scores) - 1) // 2]


if __name__ == "__main__":
    lines = [line.strip() for line in sys.stdin]

    print(part_1(lines))
    print(part_2(lines))
