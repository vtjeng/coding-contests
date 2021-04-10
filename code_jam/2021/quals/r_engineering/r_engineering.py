#!/usr/bin/env python3
from functools import lru_cache


def get_vals(s):
    return list(map(int, s.strip().split()))


@lru_cache(maxsize=None)
def get_magic_list(n, c):
    if n == 1:
        if c == 0:
            return [n]
        else:
            return None
    if c + 1 < n:
        # cost is too low
        return None
    if c + 1 > n * (n + 1) / 2:
        # cost is too high
        return None
    cur_at_end = get_magic_list(n - 1, c - n)
    cur_at_start = get_magic_list(n - 1, c - 1)
    if cur_at_start is None:
        if cur_at_end is None:
            raise ValueError(f"n:{n}, c:{c}")
        return cur_at_end[::-1] + [n]
    else:
        return [n] + cur_at_start


def process(case):
    n, c = get_vals(case)
    l = get_magic_list(n, c)
    if l is None:
        return "IMPOSSIBLE"
    else:
        return " ".join([str(n + 1 - x) for x in l])


# n = 3
# for c in range(int(n * n + 1 / 2 + 1)):
#     l = process(f"{n} {c}")
#     print(f"n={n}, c={c}, l={l}")

# Option B: Single line per case
num_cases = int(input())
for i in range(num_cases):
    print(f"Case #{i+1}: {process(input())}")
