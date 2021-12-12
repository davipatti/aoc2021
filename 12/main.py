#!/usr/bin/env python3

import sys
from collections import defaultdict, deque
from functools import lru_cache


@lru_cache
def is_lower(string):
    return string == string.lower()


def is_valid_part_1(node, existing):
    return False if (node in existing) and is_lower(node) else True


def is_valid_part_2(node, existing):
    if node not in existing or not is_lower(node):
        return True
    else:
        # If there any small caves that have been visited twice, return False
        small_caves = [cave for cave in existing if is_lower(cave)]
        return len(small_caves) == len(set(small_caves))


class CaveSystem:
    def __init__(self, pairs):
        self.adjacent = defaultdict(set)
        for a, b in pairs:
            if a != "end" and b != "start":
                self.adjacent[a].add(b)
            if a != "start" and b != "end":
                self.adjacent[b].add(a)

        self.n_paths = 0

    def visit(self, node, valid, path):
        """
        Recursively visit child nodes.

        node: visit this node, adding it to the current path
        valid: callable testing if it's valid to visit a node given the existing path
        path: history of nodes that have been visited
        """
        path.append(node)
        if node == "end":
            self.n_paths += 1
        else:
            children = [child for child in self.adjacent[node] if valid(child, path)]
            for child in children:
                self.visit(child, valid, path)
        path.pop()


def find_paths(pairs, child_valid):
    cs = CaveSystem(pairs)
    cs.visit("start", child_valid, deque())
    return cs.n_paths


if __name__ == "__main__":
    pairs = [line.strip().split("-") for line in sys.stdin]

    print(find_paths(pairs, is_valid_part_1))
    print(find_paths(pairs, is_valid_part_2))
