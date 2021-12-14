#!/usr/bin/env python3

import sys
import re
from collections import Counter


class Polymer:
    def __init__(self, lines):

        # starting string
        self.start = lines[0]

        # counts of each pair
        self.start_counts = Counter(
            (self.start[i], self.start[i + 1]) for i in range(len(self.start) - 1)
        )

        # map each pair to two new pairs
        # if F is inserted between HO, the entry for HO would be:
        # {('H', 'O'): (('H', 'F'), ('F', 'O')), ...}
        self.rules = {}
        for line in lines[2:]:
            match = re.match(r"(\w)(\w) -> (\w)", line)
            a, b, insert = match.groups()
            self.rules[(a, b)] = (a, insert), (insert, b)

    def apply_rules(self, pair_counts):
        new_pair_counts = Counter()
        for pair in pair_counts:
            for new_pair in self.rules[pair]:
                new_pair_counts[new_pair] += pair_counts[pair]
        return new_pair_counts

    def apply_rules_n(self, pair_counts, n):
        for _ in range(n):
            pair_counts = self.apply_rules(pair_counts)
        return pair_counts

    def item_counts(self, pair_counts):
        solo = Counter()
        for pair in pair_counts:
            for item in pair:
                solo[item] += pair_counts[pair]

        # all items are counted twice, except the start and end
        # add one to the start and end counts, then return everything halved
        solo[self.start[0]] += 1
        solo[self.start[-1]] += 1

        return Counter({k: v // 2 for k, v in solo.items()})

    def score(self, counts):
        values = self.item_counts(counts).values()
        return max(values) - min(values)


def part_1(poly):
    counts = poly.apply_rules_n(poly.start_counts, n=10)
    return poly.score(counts)


def part_2(poly):
    counts = poly.apply_rules_n(poly.start_counts, n=40)
    return poly.score(counts)


if __name__ == "__main__":
    poly = Polymer([line.strip() for line in sys.stdin])
    print(part_1(poly))
    print(part_2(poly))
