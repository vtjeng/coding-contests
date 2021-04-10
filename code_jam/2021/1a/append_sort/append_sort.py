#!/usr/bin/env python3


import sys

# courtesy https://stackoverflow.com/a/14981125/1404966
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def get_vals(s):
    return list(map(int, s.strip().split()))


def append_sort(x1, x2):
    if x1 < x2:
        return x2, 0
    else:
        n1 = len(str(x1))
        n2 = len(str(x2))
        assert n1 >= n2
        x1_prefix = (x1 + 1) // (10 ** (n1 - n2))
        if x2 == x1_prefix:
            return x1 + 1, (n1 - n2)
        if x2 > x1_prefix:
            return x2 * (10 ** (n1 - n2)), (n1 - n2)
        return x2 * (10 ** (n1 - n2 + 1)), (n1 - n2) + 1


def process(case):
    assert len(case) >= 2
    x_cur = case[0]
    x_sorted = [x_cur]
    count = 0
    for x in case[1:]:
        x_cur, c = append_sort(x_cur, x)
        count += c
        x_sorted.append(x_cur)
    assert sorted(x_sorted) == x_sorted
    eprint(x_sorted)
    return count


## Comment out the appropriate option
# Option A: Multiple lines per case
num_cases = int(input())
for i in range(num_cases):
    n = int(input())
    xs = get_vals(input())
    print(f"Case #{i+1}: {process(xs)}")
