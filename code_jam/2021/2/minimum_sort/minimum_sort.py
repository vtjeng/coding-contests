#!/usr/bin/env python3


# import sys

# # courtesy https://stackoverflow.com/a/14981125/1404966
# def eprint(*args, **kwargs):
#     print(*args, file=sys.stderr, **kwargs)


def get_vals(s):
    return list(map(int, s.strip().split()))


t, n, = get_vals(input())

"""
t: test cases
n: number of integers
"""
for case_id in range(t):
    for x in range(1, n):
        print(f"M {x} {n}")
        idx = int(input())
        if x != idx:
            print(f"S {x} {idx}")
            ret_code = int(input())
            if ret_code != 1:
                break
    print("D")
    ret_code = int(input())
    if ret_code != 1:
        break
