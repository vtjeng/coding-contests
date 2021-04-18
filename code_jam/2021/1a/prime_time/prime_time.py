#!/usr/bin/env python3

import sys
import math
from collections import Counter

# courtesy https://stackoverflow.com/a/14981125/1404966
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def get_vals(s):
    return list(map(int, s.strip().split()))


SMALL_PRIMES = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101,
    103,
    107,
    109,
    113,
    127,
    131,
    137,
    139,
    149,
    151,
    157,
    163,
    167,
    173,
    179,
    181,
    191,
    193,
    197,
    199,
    211,
    223,
    227,
    229,
    233,
    239,
    241,
    251,
    257,
    263,
    269,
    271,
    277,
    281,
    283,
    293,
    307,
    311,
    313,
    317,
    331,
    337,
    347,
    349,
    353,
    359,
    367,
    373,
    379,
    383,
    389,
    397,
    401,
    409,
    419,
    421,
    431,
    433,
    439,
    443,
    449,
    457,
    461,
    463,
    467,
    479,
    487,
    491,
    499,
]


def prime_factorize_small(x):
    factors = []
    for p in SMALL_PRIMES:
        while x % p == 0:
            factors.append(p)
            x //= p
    if x == 1:
        return factors
    # there is a factor larger than 499
    return None


def process(case):
    p_to_n = Counter(dict(case))
    max_sum = sum([p * n for (p, n) in case])
    # if we pick the smallest prime, picking max_product_cards + 1 of them will
    # cause us to exceed max_sum
    max_product_cards = math.floor(math.log(max_sum) / math.log(min(p_to_n)))
    # the sum can be reduced by at most this
    sum_max_reduction = max(p_to_n) * max_product_cards

    for sum_candidate in reversed(range(max_sum - sum_max_reduction, max_sum)):
        if sum_candidate <= 1:
            continue
        sum_factors = prime_factorize_small(sum_candidate)
        if sum_factors is None:
            continue
        if sum(sum_factors) + sum_candidate == max_sum:
            p_to_m = Counter(sum_factors)
            for p, m in p_to_m.items():
                if m <= p_to_n[p]:
                    # we have enough of these factors
                    return sum_candidate
    return 0


## Comment out the appropriate option
# Option A: Multiple lines per case
num_cases = int(input())
for i in range(num_cases):
    num_distinct_primes = int(input())
    case = []
    for j in range(num_distinct_primes):
        case.append(tuple(get_vals(input())))
    print(f"Case #{i+1}: {process(case)}")
