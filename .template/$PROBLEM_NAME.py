#!/usr/bin/env python3


import sys

# courtesy https://stackoverflow.com/a/14981125/1404966
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def get_vals(s):
    return list(map(int, s.strip().split()))


def process(case):
    pass


## Comment out the appropriate option
# Option A: Multiple lines per case
num_cases = int(input())
for i in range(num_cases):
    num_case_lines = int(input())
    case = []
    for j in range(num_case_lines):
        case.append(input())
    print(f"Case #{i+1}: {process(case)}")

# Option B: Single line per case
num_cases = int(input())
for i in range(num_cases):
    print(f"Case #{i+1}: {process(input())}")
