#!/usr/bin/env python3

from functools import lru_cache


class InvalidQueryError(Exception):
    pass


def get_vals(s):
    return list(map(int, s.strip().split()))


def get_median(xs):
    return _get_median(*sorted(xs))


@lru_cache(maxsize=None)
def _get_median(a, b, c):
    xs = [a, b, c]
    print(" ".join(map(str, xs)))
    r = int(input())
    if r == -1:
        raise InvalidQueryError
    assert r in xs
    return r


def find_insertion_index(xs, x):
    """Returns the number of elements in xs that x should be inserted after
    such that xs is maintained in sorted order. 

    Parameters
    ----------
    xs : List[int]
        List of indexes; expected to be sorted
    x : int
    """
    n = len(xs)
    assert n != 1
    if n == 0:
        return 0
    if n == 2:
        m = get_median([xs[0], xs[1], x])
        if m == xs[0]:
            return 0
        if m == x:
            return 1
        if m == xs[1]:
            return 2
    j = (n - 1) // 2
    m = get_median([xs[j], xs[j + 1], x])
    if m == x:
        return j + 1
    elif m == xs[j]:
        if len(xs[:j]) == 1:
            return find_insertion_index(xs[: j + 1], x)
        return find_insertion_index(xs[:j], x)
    elif m == xs[j + 1]:
        if len(xs[j + 2 :]) == 1:
            return find_insertion_index(xs[j + 1 :], x) + j + 1
        return find_insertion_index(xs[j + 2 :], x) + j + 2
    else:
        raise AssertionError


def sort(indexes):
    """
    Parameters
    ----------
    indexes : List[Integer]
    """
    if len(indexes) < 3:
        return indexes
    i1, i2, i3 = indexes[:3]
    pivot = get_median([i1, i2, i3])
    if pivot == i1:
        sorted_indexes = [i2, i1, i3]
    elif pivot == i2:
        sorted_indexes = [i1, i2, i3]
    elif pivot == i3:
        sorted_indexes = [i1, i3, i2]
    else:
        raise AssertionError
    for i in indexes[3:]:
        j = find_insertion_index(sorted_indexes, i)
        sorted_indexes = sorted_indexes[:j] + [i] + sorted_indexes[j:]
    return sorted_indexes


total_cases, n, q = get_vals(input())
for case in range(total_cases):
    _get_median.cache_clear()
    try:
        sorted_indexes = sort(list(range(1, n + 1)))
    except InvalidQueryError:
        break
    print(" ".join(map(str, sorted_indexes)))
    r = input()
    if r == -1:
        break

"""
$ python interactive_runner.py python3 testing_tool.py 0 -- python3 median_sort.py
judge: Total Queries Used: 1492/30000

$ python interactive_runner.py python3 testing_tool.py 1 -- python3 median_sort.py
judge: Total Queries Used: 16213/30000

$ python interactive_runner.py python3 testing_tool.py 2 -- python3 median_sort.py
judge: Total Queries Used: 16324/17000
"""
