#!/usr/bin/env python3

import sys

# courtesy https://stackoverflow.com/a/14981125/1404966
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def get_vals(s):
    return list(map(int, s.strip().split()))


def get_maximum_exponent(ps, ns):
    # everything in the left hand
    cur_sum = sum([p * n for (p, n) in zip(ps, ns)])

    # find the maximum exponent we need to look at
    cur_prod = 1
    cur_exp_count = 0
    for (p, n) in zip(ps, ns):
        for _ in range(n):
            if cur_prod >= cur_sum:
                return cur_exp_count
            cur_exp_count += 1
            cur_prod *= p
            cur_sum -= p
            eprint(cur_prod)
    return cur_exp_count


def helper(ps, ns, cur_sum, cur_prod):
    if cur_sum == cur_prod:
        return cur_sum
    assert len(ps) == len(ns)
    if len(ps) == 0:
        return 0
    if cur_sum < cur_prod:
        return 0
    p = ps[-1]
    n = ns[-1]
    return max(
        helper(ps[:-1], ns[:-1], cur_sum - p * m, cur_prod * (p ** m))
        for m in range(n + 1)
    )


def process(case):
    ps = []
    ns = []
    for (p, n) in case:
        ps.append(p)
        ns.append(n)
    max_sum = sum([p * n for (p, n) in zip(ps, ns)])
    return helper(ps, ns, max_sum, 1)


## Comment out the appropriate option
# Option A: Multiple lines per case
num_cases = int(input())
for i in range(num_cases):
    num_distinct_primes = int(input())
    case = []
    for j in range(num_distinct_primes):
        case.append(tuple(get_vals(input())))
    print(f"Case #{i+1}: {process(case)}")
