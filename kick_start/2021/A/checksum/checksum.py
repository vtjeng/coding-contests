#!/usr/bin/env python3


import numpy as np


def get_vals(s):
    return list(map(int, s.strip().split()))


def get_mst(A, V):
    """
    Parameters
    ----------
    A : np.array
    """
    n = len(A)
    # for each vertex, we track the closest vertex in the MST, as well as
    # the distance to that vertex
    distance_to_mst = [float("inf")] * n
    closest_mst_vertex = [None] * n
    unvisited = set(V)
    mst = set()
    while len(unvisited) > 0:
        # we search for a vertex that
        v = None
        for j, d in enumerate(distance_to_mst):
            if j in unvisited:
                if v is None and distance_to_mst[j] != float("inf"):
                    v = j
                if v is not None and distance_to_mst[j] < distance_to_mst[v]:
                    v = j

        if v is None:
            # remaining unvisited vertices are not connected to MST
            v = unvisited.pop()
        else:
            unvisited.remove(v)
            mst.add(tuple(sorted((v, closest_mst_vertex[v]))))

        for u, d in enumerate(A[v]):
            if d < distance_to_mst[u]:
                distance_to_mst[u] = d
                closest_mst_vertex[u] = v
    return mst


def process(adj, edge_cost, vertices):
    if len(vertices) == 0:
        # whole graph is already known
        return 0
    mst = get_mst(adj, vertices)
    cost = 0
    for e, c in edge_cost.items():
        if e not in mst:
            cost += c
    return cost


## Comment out the appropriate option
# Option A: Multiple lines per case
num_cases = int(input())
for case_id in range(num_cases):
    n = int(input())
    missing_cells = set()
    adj = np.ones((2 * n, 2 * n)) * float("inf")
    edge_cost = dict()
    vertices = set()
    for i in range(n):
        for j, e in enumerate(get_vals(input())):
            if e == -1:
                missing_cells.add((i, j))
    for i in range(n):
        for j, c in enumerate(get_vals(input())):
            if (i, j) in missing_cells:
                # only need to take note of those cells that are
                adj[i][j + n] = -c
                adj[j + n][i] = -c
                edge_cost[(i, j + n)] = c
                vertices.add(i)
                vertices.add(j + n)
    # row checksums
    input()
    # column checksums
    input()
    print(f"Case #{case_id+1}: {process(adj, edge_cost, vertices)}")
