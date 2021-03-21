#!/usr/bin/env python3


from collections import defaultdict
import numpy as np


def get_vals(s):
    return list(map(int, s.strip().split()))


from collections.abc import MutableMapping


class heapdict(MutableMapping):
    __marker = object()

    def __init__(self, *args, **kw):
        self.heap = []
        self.d = {}
        self.update(*args, **kw)

    def clear(self):
        del self.heap[:]
        self.d.clear()

    def __setitem__(self, key, value):
        if key in self.d:
            self.pop(key)
        wrapper = [value, key, len(self)]
        self.d[key] = wrapper
        self.heap.append(wrapper)
        self._decrease_key(len(self.heap) - 1)

    def _min_heapify(self, i):
        n = len(self.heap)
        h = self.heap
        while True:
            # calculate the offset of the left child
            l = (i << 1) + 1
            # calculate the offset of the right child
            r = (i + 1) << 1
            if l < n and h[l][0] < h[i][0]:
                low = l
            else:
                low = i
            if r < n and h[r][0] < h[low][0]:
                low = r

            if low == i:
                break

            self._swap(i, low)
            i = low

    def _decrease_key(self, i):
        while i:
            # calculate the offset of the parent
            parent = (i - 1) >> 1
            if self.heap[parent][0] < self.heap[i][0]:
                break
            self._swap(i, parent)
            i = parent

    def _swap(self, i, j):
        h = self.heap
        h[i], h[j] = h[j], h[i]
        h[i][2] = i
        h[j][2] = j

    def __delitem__(self, key):
        wrapper = self.d[key]
        while wrapper[2]:
            # calculate the offset of the parent
            parentpos = (wrapper[2] - 1) >> 1
            parent = self.heap[parentpos]
            self._swap(wrapper[2], parent[2])
        self.popitem()

    def __getitem__(self, key):
        return self.d[key][0]

    def __iter__(self):
        return iter(self.d)

    def popitem(self):
        """D.popitem() -> (k, v), remove and return the (key, value) pair with lowest\nvalue; but raise KeyError if D is empty."""
        wrapper = self.heap[0]
        if len(self.heap) == 1:
            self.heap.pop()
        else:
            self.heap[0] = self.heap.pop()
            self.heap[0][2] = 0
            self._min_heapify(0)
        del self.d[wrapper[1]]
        return wrapper[1], wrapper[0]

    def __len__(self):
        return len(self.d)

    def peekitem(self):
        """D.peekitem() -> (k, v), return the (key, value) pair with lowest value;\n but raise KeyError if D is empty."""
        return (self.heap[0][1], self.heap[0][0])


def get_mst(A, V):
    """
    Parameters
    ----------
    A : np.array
    """
    closest_mst_vertex = {v: None for v in V}
    unvisited_distances = heapdict({v: float("inf") for v in V})
    mst = set()
    while len(unvisited_distances) > 0:
        v, d = unvisited_distances.popitem()
        if d != float("inf"):
            mst.add(tuple(sorted((v, closest_mst_vertex[v]))))

        for u in set(unvisited_distances):
            # for u, d in enumerate(A[v]):
            #     if u in unvisited_distances and d < unvisited_distances[u]:
            d = A[v][u]
            if d < unvisited_distances[u]:
                unvisited_distances[u] = d
                closest_mst_vertex[u] = v
    return mst


def process(adj, edge_cost, total_cost, vertices):
    if len(vertices) == 0:
        # whole graph is already known
        return 0
    mst = get_mst(adj, vertices)
    cost = total_cost
    for e in mst:
        cost -= edge_cost[e]
    return cost


## Comment out the appropriate option
# Option A: Multiple lines per case
num_cases = int(input())
for case_id in range(num_cases):
    n = int(input())
    missing_cells = set()
    adj = np.ones((2 * n, 2 * n)) * float("inf")
    edge_cost = dict()
    total_cost = 0
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
                total_cost += c
                vertices.add(i)
                vertices.add(j + n)
    # row checksums
    input()
    # column checksums
    input()
    print(f"Case #{case_id+1}: {process(adj, edge_cost, total_cost, vertices)}")
