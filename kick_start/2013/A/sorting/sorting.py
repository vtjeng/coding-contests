#!/usr/bin/env python3


def process(case):
    # odd numbers in increasing order
    # even numbers in decreasing order
    # slots taken by odd numbers continue to be odd
    xs = list(map(int, case.strip().split()))
    odds = list(filter(lambda x: x % 2 == 1, xs))
    evens = list(filter(lambda x: x % 2 == 0, xs))
    odds_sorted_rev = sorted(odds, reverse=True)
    evens_sorted_rev = sorted(evens)

    xs_sorted_special = []
    for x in xs:
        if x % 2 == 1:
            x_new = odds_sorted_rev.pop()
        else:
            x_new = evens_sorted_rev.pop()
        xs_sorted_special.append(x_new)
    return " ".join(map(str, xs_sorted_special))


## Comment out the appropriate option
# Option A: Multiple lines per case
num_cases = int(input())
for i in range(num_cases):
    num_vals = int(input())
    print(f"Case #{i+1}: {process(input())}")
