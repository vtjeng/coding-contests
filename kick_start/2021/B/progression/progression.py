#!/usr/bin/env python3


import sys

# courtesy https://stackoverflow.com/a/14981125/1404966
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def get_vals(s):
    return list(map(int, s.strip().split()))


def longest_arithmetic_subarray(xs):
    max_length = 2
    # current candidate subarray is [i, j)
    i = 0
    for j in range(2, len(xs)):
        if not (xs[j] - xs[j - 1] == xs[i + 1] - xs[i]):
            cur_length = j - i
            max_length = max(cur_length, max_length)
            i = j - 1
    return max(max_length, j + 1 - i)


def _mid_helper(xs, i):
    d = (xs[i + 1] - xs[i - 1]) // 2
    a = i - 1
    b = i + 1
    count = 3
    while a > 0 and xs[a] - xs[a - 1] == d:
        a -= 1
        count += 1
    while b < len(xs) - 1 and xs[b + 1] - xs[b] == d:
        b += 1
        count += 1
    return count


def process(xs):
    n = len(xs)
    if n <= 3:
        # always possible to make an arithmetic progression of at least the length of the array
        return n

    return max(
        min(n, longest_arithmetic_subarray(xs) + 1),
        *[_mid_helper(xs, i) for i in range(1, len(xs) - 1)],
    )


# Option B: Single line per case
num_cases = int(input())
for i in range(num_cases):
    n = input()
    print(f"Case #{i+1}: {process(get_vals(input()))}")
