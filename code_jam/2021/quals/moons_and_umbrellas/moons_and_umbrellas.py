#!/usr/bin/env python3


# from typing import List
# from functools import lru_cache


# @lru_cache(maxsize=None)
def get_prefix_score(is_c, n, x, y):
    if n == 0:
        return 0
    return min(get_infix_score(is_c1, is_c, n - 1, x, y) for is_c1 in (True, False))


# @lru_cache(maxsize=None)
def get_suffix_score(is_c, n, x, y):
    if n == 0:
        return 0
    return min(get_infix_score(is_c, is_c2, n - 1, x, y) for is_c2 in (True, False))


# @lru_cache(maxsize=None)
def get_infix_score(is_c1, is_c2, n, x, y):
    score = 0
    if is_c1 and not is_c2:
        score += x
    if not is_c1 and is_c2:
        score += y
    if x + y < 0:
        if is_c1 == is_c2:
            score += (n + 1) // 2 * (x + y)
        else:
            score += n // 2 * (x + y)
    return score


def process(case):
    x, y, s = case.split()
    x = int(x)
    y = int(y)

    score = 0

    last_fixed_symbol = None
    n = 0
    for c in s:
        if c == "?":
            n += 1
        else:
            if last_fixed_symbol is None:
                score += get_prefix_score(c == "C", n, x, y)
            else:
                score += get_infix_score(last_fixed_symbol == "C", c == "C", n, x, y)
            n = 0
            last_fixed_symbol = c
    score += get_suffix_score(last_fixed_symbol == "C", n, x, y)
    return score


num_cases = int(input())
for i in range(num_cases):
    print(f"Case #{i+1}: {process(input())}")
