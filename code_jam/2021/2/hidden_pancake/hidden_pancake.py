#!/usr/bin/env python3

import functools
import sys
from itertools import tee
from collections import defaultdict

MOD = 1000000007

MOD_FACTORIALS = [1]
MOD_INV_FACTORIALS = [1]

for i in range(1, int(10 ** 5)):
    MOD_FACTORIALS.append(MOD_FACTORIALS[-1] * i % MOD)
    MOD_INV_FACTORIALS.append(MOD_INV_FACTORIALS[-1] * pow(i, MOD - 2, MOD) % MOD)


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


@functools.lru_cache(maxsize=None)
def multinomial(xs):
    c = MOD_FACTORIALS[sum(xs)]
    for x in xs:
        c *= MOD_INV_FACTORIALS[x]
        c = c % MOD
    return c


# courtesy https://stackoverflow.com/a/14981125/1404966
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def get_vals(s):
    return list(map(int, s.strip().split()))


# v points to u if v > u. we call v u's "parent"


def p_to_c(v_to_parent_vertex):
    v_to_child_vertices = defaultdict(set)
    for v, parent_vertex in v_to_parent_vertex.items():
        v_to_child_vertices[parent_vertex].add(v)
        # touch all vertices to ensure that they have a list of length 0
        v_to_child_vertices[v]
    return v_to_child_vertices


def get_topological_sort_order(v_to_parent_vertex):
    v_to_child_vertices = p_to_c(v_to_parent_vertex)
    childless_nodes = []

    # find a list of 'start nodes' with no incoming edges
    for v, children in v_to_child_vertices.items():
        if len(children) == 0:
            childless_nodes.append(v)

    while len(childless_nodes) > 0:
        v = childless_nodes.pop()
        yield v
        parent_vertex = v_to_parent_vertex[v]
        v_to_child_vertices[parent_vertex].remove(v)
        if len(v_to_child_vertices[parent_vertex]) == 0:
            childless_nodes.append(parent_vertex)


def get_count(v_to_parent_vertex):
    v_to_child_vertices = p_to_c(v_to_parent_vertex)
    v_to_subtree_size = defaultdict(lambda: 1)
    count = 1
    for v in get_topological_sort_order(v_to_parent_vertex):
        if v is None:
            break
        child_vertices = v_to_child_vertices[v]
        child_subtree_sizes = [v_to_subtree_size[u] for u in child_vertices]
        v_to_subtree_size[v] = 1 + sum(child_subtree_sizes)
        if len(child_vertices) <= 1:
            continue
        count *= multinomial(tuple(sorted(child_subtree_sizes)))
        count = count % MOD
    return count


def process(visible_counts, visibles_sorted=[None] * int(10 ** 5)):
    # to avoid re-allocations, we re-use the `visibles_sorted` list.
    # the first num_visible elements of visibles_sorted are valid
    # they are the current visible pancakes, in decreasing order of size
    num_visible = 0
    v_to_parent_vertex = dict()
    for idx, c in enumerate(visible_counts):
        # check for impossible visible count
        if c > num_visible + 1:
            # can add only 1 pancake, but visible count increased by more than 1
            return 0

        # if one or more pancakes were hidden, edit parent for the largest hidden pancake
        if c < num_visible + 1:
            v_to_parent_vertex[visibles_sorted[c - 1]] = idx

        # specify parent for added pancake
        v_to_parent_vertex[idx] = None if c == 1 else visibles_sorted[c - 2]

        # update number of visible pancakes
        num_visible = c

        # modify the cth visible pancake (the one just added)
        visibles_sorted[c - 1] = idx
    return get_count(v_to_parent_vertex)


## Comment out the appropriate option
# Option A: Multiple lines per case
num_cases = int(input())
for i in range(num_cases):
    n = int(input())
    visible_counts = get_vals(input())
    print(f"Case #{i+1}: {process(visible_counts)}")

