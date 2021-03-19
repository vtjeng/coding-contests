#!/usr/bin/env python3


def get_vals(s):
    return list(map(int, s.strip().split()))


def get_element(n):
    p = 1
    q = 1
    for e in list(map(int, list(bin(n)[3:]))):
        if e == 1:
            p = p + q
        else:
            q = p + q
    return (p, q)


def get_position(p, q):
    if p == 1 and q == 1:
        return 1
    if p > q:
        return 2 * get_position(p - q, q) + 1
    return 2 * get_position(p, q - p)


def process(case):
    vals = get_vals(case)
    if vals[0] == 1:
        return " ".join(map(str, get_element(vals[1])))
    if vals[0] == 2:
        return str(get_position(vals[1], vals[2]))


# Option B: Single line per case
num_cases = int(input())
for i in range(num_cases):
    print(f"Case #{i+1}: {process(input())}")
