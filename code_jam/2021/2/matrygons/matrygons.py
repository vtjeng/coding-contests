#!/usr/bin/env python3


import sys
import functools

# courtesy https://stackoverflow.com/a/14981125/1404966
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


PRIMES = (
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
    503,
    509,
    521,
    523,
    541,
    547,
    557,
    563,
    569,
    571,
    577,
    587,
    593,
    599,
    601,
    607,
    613,
    617,
    619,
    631,
    641,
    643,
    647,
    653,
    659,
    661,
    673,
    677,
    683,
    691,
    701,
    709,
    719,
    727,
    733,
    739,
    743,
    751,
    757,
    761,
    769,
    773,
    787,
    797,
    809,
    811,
    821,
    823,
    827,
    829,
    839,
    853,
    857,
    859,
    863,
    877,
    881,
    883,
    887,
    907,
    911,
    919,
    929,
    937,
    941,
    947,
    953,
    967,
    971,
    977,
    983,
    991,
    997,
)


def prime_factorize(n):
    prime_factors = []
    for p in PRIMES:
        if p * p > n:
            break
        count = 0
        while n % p == 0:
            n //= p
            count += 1
        if count > 0:
            prime_factors.append((p, count))
    if n > 1:
        prime_factors.append((n, 1))
    return prime_factors


def divisors(n):
    ds = [1]
    for prime, count in prime_factorize(n):
        ds += [x * prime ** k for k in range(1, count + 1) for x in ds]
    return ds


@functools.lru_cache(maxsize=None)
def decompose(x, min_val=2):
    """Returns the maximum number of terms `x` can be decomposed into.

    A decomposition into k terms is valid if it satisfied the following constraints:

    (1)   x = a_1 + a_2 + ... + a_k 
    (2)   For all 1 <= i < j <= k, a_j | a_i (in particular, a_(i+1) | a_i)
    (3)   a_1 >= min_val
    """
    if x < min_val:
        return 0
    best_n = 1
    for d in divisors(x):
        if d >= min_val:
            this_n = decompose(x // d - 1) + 1
            best_n = max(best_n, this_n)
    return best_n


def process(x):
    return decompose(x, min_val=3)


# Option B: Single line per case
num_cases = int(input())
for i in range(num_cases):
    print(f"Case #{i+1}: {process(int(input()))}")
