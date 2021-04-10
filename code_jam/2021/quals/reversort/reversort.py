#!/usr/bin/env python3


def get_vals(s):
    return list(map(int, s.strip().split()))


def process(l):
    l_sorted = sorted(l)
    c = 0
    for rank in range(len(l) - 1):
        # print(l)
        e = l_sorted[rank]
        idx = l.index(e)
        c += (idx - rank) + 1
        # print(c)
        # print(l[:rank], l[idx : rank - 1 : -1], l[idx + 1 :])
        l = l[:rank] + l[rank : idx + 1][::-1] + l[idx + 1 :]
    return c


num_cases = int(input())
for i in range(num_cases):
    n = int(input())
    l = get_vals(input())
    print(f"Case #{i+1}: {process(l)}")
