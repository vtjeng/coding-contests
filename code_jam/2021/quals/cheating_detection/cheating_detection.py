#!/usr/bin/env python3
import numpy as np


BIG_M = 1000

import sys


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def get_vals(s):
    return list(map(int, s.strip().split()))


def process(case):
    p_q = np.mean(case, axis=0)
    p_s = np.mean(case, axis=1)
    correct_difficulty_s = np.divide(
        np.sum(np.multiply(p_q, case), axis=1), np.sum(case, axis=1)
    )
    incorrect_difficulty_s = np.divide(
        np.sum(np.multiply(p_q, 1 - case), axis=1), np.sum(1 - case, axis=1)
    )
    delta_difficulty_s = correct_difficulty_s - incorrect_difficulty_s
    return np.argmin(delta_difficulty_s - BIG_M * (p_s > 0.45)) + 1


## Comment out the appropriate option
# Option A: Multiple lines per case
num_cases = int(input())
percentage_threshold = int(input())
for i in range(num_cases):
    case = []
    for _ in range(100):
        case.append([int(x) for x in input()])
    print(f"Case #{i+1}: {process(np.array(case))}")
