#!/usr/bin/env python3


def process(case):
    max_seen = case[0]
    c = 0
    for card in case:
        if card < max_seen:
            c += 1
        else:
            max_seen = card
    return c


## Comment out the appropriate option
# Option A: Multiple lines per case
num_cases = int(input())
for i in range(num_cases):
    num_case_lines = int(input())
    case = []
    for j in range(num_case_lines):
        case.append(input())
    print(f"Case #{i+1}: {process(case)}")
