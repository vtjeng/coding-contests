#!/usr/bin/env python3


def get_vals(s):
    return list(map(int, s.strip().split()))


def get_goodness(s):
    goodness = 0
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[-(i + 1)]:
            goodness += 1
    return goodness


def process(n, k, s):
    return abs(k - get_goodness(s))


## Comment out the appropriate option
# Option A: Multiple lines per case
num_cases = int(input())
for i in range(num_cases):
    n, k = get_vals(input())
    s = input()
    print(f"Case #{i+1}: {process(n, k, s)}")
