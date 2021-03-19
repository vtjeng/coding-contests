#!/usr/bin/env python3

import math


def get_launch_angle(v, d):
    t_rad = 0.5 * math.asin(max(min(9.8 * d / (v ** 2), 1), -1))
    return t_rad * 180 / math.pi


num_cases = int(input())
for i in range(num_cases):
    v, d = list(map(int, input().strip().split()))
    print(f"Case #{i+1}: {get_launch_angle(v, d):.7f}")

