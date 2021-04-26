#!/usr/bin/env python3


import sys

import math
from typing import List

# courtesy https://stackoverflow.com/a/14981125/1404966
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def get_vals(s):
    return list(map(int, s.strip().split()))


def clear(counts):
    while len(counts) > 0 and counts[-1] == 0:
        counts.pop()


def expand(counts: List[int], a: int, b: int):
    if len(counts) == 0:
        return
    j = len(counts) - 1
    v = counts.pop()
    if j - a >= 0:
        counts[j - a] += v
    if j - b >= 0:
        counts[j - b] += v


def is_covering_stack(counts1: List[int], counts2: List[int], a: int, b: int):
    """Check if the count of metals in counts1 "covers" that in counts2
    """
    eprint(counts1, counts2)
    while len(counts1) >= len(counts2):
        for i in range(len(counts2)):
            overlap = min(counts1[i], counts2[i])
            counts1[i] -= overlap
            counts2[i] -= overlap
        clear(counts1)
        clear(counts2)
        if len(counts2) == 0:
            eprint("")
            return True
        expand(counts1, a, b)
        eprint(counts1, counts2)
    eprint("")
    return False


def is_identical(xs):
    if len(xs) == 0:
        return True
    return all(x == xs[0] for x in xs)


def process(n, a, b, counts):
    assert len(counts) == n
    d = math.gcd(a, b)
    nonzero_ids = [i + 1 for i, c in enumerate(counts) if c > 0]
    nonzero_id_remainders = [i % d for i in nonzero_ids]
    if not is_identical(nonzero_id_remainders):
        return "IMPOSSIBLE"
    r = nonzero_id_remainders[0]

    m = d * (n // d) + r
    while True:
        counts1 = [0] * m
        counts1[m - 1] = 1
        if is_covering_stack(counts1, counts[::], a, b):
            return m
        m += d


## Comment out the appropriate option
# Option A: Multiple lines per case
num_cases = int(input())
for i in range(num_cases):
    n, a, b = get_vals(input())
    counts = get_vals(input())
    print(f"Case #{i+1}: {process(n, a, b, counts)}")

