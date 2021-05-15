#!/usr/bin/env python3


import sys
import numpy as np

# courtesy https://stackoverflow.com/a/14981125/1404966
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def get_vals(s):
    return list(map(int, s.strip().split()))


def get_pairs_idxs(r, c):
    for i in range(r):
        for j in range(c - 1):
            yield ((i, j), (i, j + 1))
    for i in range(r - 1):
        for j in range(c):
            yield ((i, j), (i + 1, j))


def process(current, target, f, s):
    r, c = current.shape
    any_changed = True
    cost = 0
    while any_changed:
        any_changed = False
        for p1, p2 in get_pairs_idxs(r, c):
            c1 = current[p1]
            c2 = current[p2]
            t1 = target[p1]
            t2 = target[p2]
            if c1 != c2 and (c1, c2) == (t2, t1):
                cost += s
                any_changed = True
                current[p1] = c2
                current[p2] = c1

    return cost + f * np.sum(abs(current != target))


## Comment out the appropriate option
# Option A: Multiple lines per case
num_cases = int(input())
for i in range(num_cases):
    r, c, f, s = get_vals(input())

    cur = []
    for _ in range(r):
        cur.append(list(input()))
    cur_p = np.array(cur) == "M"

    tar = []
    for _ in range(r):
        tar.append(list(input()))
    tar_p = np.array(tar) == "M"

    print(f"Case #{i+1}: {process(cur_p, tar_p, f, s)}")

