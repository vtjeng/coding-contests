#!/usr/bin/env python3


def get_vals(s):
    return list(map(int, s.strip().split()))


def find_partition(x, par):
    if x == par[x]:
        return x
    par[x] = find_partition(par[x], par)
    return par[x]


def union(x, y, par):
    """Join the sets containing elements x and y.

    Returns
    -------
    bool
        True if x and y were initially different sets
    """
    px = find_partition(x, par)
    py = find_partition(y, par)
    if px == py:
        return False
    par[px] = py
    return True


def process():
    n = int(input())
    # `par` encapsulates a disjoin-set data structure.
    # we maintain the following invariants:
    #  - (i, par[i]) forms a forest where each (disjoint) set is a tree.
    par = list(range(2 * n))
    for _ in range(n):
        input()

    cost_to_edge = list()
    for i in range(n):
        for j, c in enumerate(get_vals(input())):
            if c > 0:
                cost_to_edge.append((c, (i, j + n)))
    # read in and ignore the row and column checksums
    input()
    input()

    # we iterate over the edges in _decreasing_ order so that we are always
    # removing the smallest cost edge
    cost_to_edge.sort(reverse=True)

    total_cost = 0
    for cost, edge in cost_to_edge:
        u, v = edge
        if not union(u, v, par):
            # the two vertices are already in the same set; we need to remove
            # it to avoid a cycle existing
            total_cost += cost
    return total_cost


## Comment out the appropriate option
# Option A: Multiple lines per case
num_cases = int(input())
for case_id in range(num_cases):
    print(f"Case #{case_id+1}: {process()}")
