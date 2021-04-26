#!/usr/bin/env python3


import sys
import itertools
import math


def triplewise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b, c = itertools.tee(iterable, 3)
    next(c, None)
    next(c, None)
    next(b, None)
    return zip(a, b, c)


def gen_primes():
    """Generator for an infinite sequence of primes
    """

    # maps composite numbers to prime 'witnesses' for their compositeness
    D = {}

    # running number being checked for primality
    n = 2

    while True:
        if n not in D:
            # n must be prime
            D[n * n] = [n]
            yield n
        else:
            # we can now remove n from D
            # we know that at this point D[n] contains all of its prime factors
            # we mark the next multiples of the witnesses of n (specifically p is a prime witness to the compositness of n+p)
            for p in D[n]:
                D.setdefault(n + p, []).append(p)
        n += 1


def is_prime(n):
    if n < 30:
        return n in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    m = math.sqrt(n)
    for p in gen_primes():
        if p > m:
            return True
        if n % p == 0:
            return False


# courtesy https://stackoverflow.com/a/14981125/1404966
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def get_vals(s):
    return list(map(int, s.strip().split()))


def process(case):
    if case < 1000:
        for p1, p2, p3 in triplewise(gen_primes()):
            if p2 * p3 > case:
                return p1 * p2

    # we are working with large numbers
    m = math.sqrt(case)
    x2 = math.ceil(m)
    if int(m) == m:
        x1 = int(m - 1)
    else:
        x1 = math.floor(m)
    if x2 % 2 == 0:
        x2 += 1
    if x1 % 2 == 0:
        x1 -= 1
    # eprint(x1, m, x2)
    # x1 is the largest odd number below m, x2 is the smallest odd number at or above m
    while not is_prime(x1):
        x1 -= 2
    x0 = x1 - 2
    while not is_prime(x0):
        x0 -= 2
    while not is_prime(x2):
        x2 += 2
    # eprint(x0, x1, x2)
    cand = x2 * x1
    if cand > case:
        return x1 * x0
    else:
        return cand


# Option B: Single line per case
num_cases = int(input())
for i in range(num_cases):
    print(f"Case #{i+1}: {process(int(input()))}")
