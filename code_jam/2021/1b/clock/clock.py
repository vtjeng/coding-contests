#!/usr/bin/env python3


import sys
import itertools

# courtesy https://stackoverflow.com/a/14981125/1404966
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def get_vals(s):
    return list(map(int, s.strip().split()))


NSECS_IN_SEC = 10 ** 9
SECS_IN_MIN = 60
MINS_IN_HRS = 60
HRS_IN_CLOCK = 12
SECS_IN_CLOCK = HRS_IN_CLOCK * MINS_IN_HRS * SECS_IN_MIN
NSECS_IN_CLOCK = SECS_IN_CLOCK * NSECS_IN_SEC

M_HOURS = 1
M_MINS = HRS_IN_CLOCK
M_SECS = M_MINS * MINS_IN_HRS

# https://stackoverflow.com/a/9758173/1404966
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception("modular inverse does not exist")
    else:
        return x % m


MODINV_M_MINS_MINUS_ONE = modinv(M_MINS - 1, NSECS_IN_CLOCK)
MODINV_M_SECS_MINUS_ONE = modinv(M_SECS - 1, NSECS_IN_CLOCK)


def disp_time(t):
    nsecs = t % NSECS_IN_SEC
    seconds = (t // NSECS_IN_SEC) % SECS_IN_MIN
    minutes = (t // (NSECS_IN_SEC * SECS_IN_MIN)) % MINS_IN_HRS
    hours = (t // (NSECS_IN_SEC * SECS_IN_MIN * MINS_IN_HRS)) % HRS_IN_CLOCK
    return f"{hours} {minutes} {seconds} {nsecs}"


def get_delta(h_ticks, m_ticks, s_ticks):
    delta_for_mins = (
        (m_ticks - h_ticks * M_MINS) * MODINV_M_MINS_MINUS_ONE % NSECS_IN_CLOCK
    )
    delta_for_secs = (
        (s_ticks - h_ticks * M_SECS) * MODINV_M_SECS_MINUS_ONE % NSECS_IN_CLOCK
    )
    if delta_for_secs == delta_for_mins:
        return delta_for_secs
    return None


def process(xs):
    """xs are the angles of each hand, relative to an arbitrary axis in the clockwise direction

    1 tick is equal to 1/12×10−10 degrees. 
    This means that the hours hand rotates exactly 1 tick each nanosecond, 
    the minutes hand rotates exactly 12 ticks each nanosecond and 
    the seconds hand rotates exactly 720 ticks each nanosecond.
    """
    for h_ticks, m_ticks, s_ticks in itertools.permutations(xs):
        d = get_delta(h_ticks, m_ticks, s_ticks)
        if d is not None:
            return disp_time(h_ticks + d)


## Comment out the appropriate option
# Option A: Multiple lines per case
# Option B: Single line per case
num_cases = int(input())
for i in range(num_cases):
    print(f"Case #{i+1}: {process(get_vals(input()))}")
