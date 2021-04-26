#!/usr/bin/env python3


import sys

# courtesy https://stackoverflow.com/a/14981125/1404966
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def get_vals(s):
    return list(map(int, s.strip().split()))


def process(case):
    pass


class StackHeights(object):
    def __init__(self, n, b):
        self.num_towers = n
        self.block_capacity = b
        self.tower_heights = [0] * n
        self.towers = [list() for _ in range(n)]

    def stack(self, i, v):
        assert 0 <= i < self.num_towers
        assert self.tower_heights[i] < self.block_capacity
        self.tower_heights[i] += 1
        # eprint(self.tower_heights)
        self.towers[i].append(v)

    def is_full(self):
        return min(self.tower_heights) == self.block_capacity

    def get_first_nonfull_tower(self, min_preferred_cap):
        assert not self.is_full()
        for i, h in enumerate(self.tower_heights):
            if h + min_preferred_cap <= self.block_capacity:
                return i
        return self.get_first_nonfull_tower(1)


t, n, b, p = get_vals(input())

"""
t: test cases
n: number of towers
b: number of blocks in each tower
p: minimum passing score
"""
cur_tower = 0
blocks_per_case = n * b
for case_id in range(t):
    sh = StackHeights(n, b)
    for block_id in range(blocks_per_case):
        x = int(input())
        if x == -1:
            break
        min_preferred_cap = 1 if x == 9 else 2
        i = sh.get_first_nonfull_tower(min_preferred_cap)
        sh.stack(i, x)
        print(i + 1)
    # eprint("")
    # eprint(sh.tower_heights)
    # eprint(sh.towers)
