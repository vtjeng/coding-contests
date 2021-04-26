#!/usr/bin/env python3


import sys
from itertools import tee


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


# courtesy https://stackoverflow.com/a/14981125/1404966
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def get_vals(s):
    return list(map(int, s.strip().split()))


def process(case):
    lengths = [1]
    for (c1, c2) in pairwise(case):
        if c2 > c1:
            cur_length = lengths[-1] + 1
            lengths.append(cur_length)
        else:
            lengths.append(1)
    return " ".join([str(x) for x in lengths])


## Comment out the appropriate option
# Option A: Multiple lines per case
num_cases = int(input())
for i in range(num_cases):
    int(input())  # string length
    print(f"Case #{i+1}: {process(input())}")
