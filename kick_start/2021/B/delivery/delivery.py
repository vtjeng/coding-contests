#!/usr/bin/env python3


from collections import defaultdict, deque
from math import gcd
from functools import reduce
import sys
import bisect
import functools

# courtesy https://stackoverflow.com/a/14981125/1404966
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def get_vals(s):
    return list(map(int, s.strip().split()))


def process(edges, queries):
    n = len(edges) + 1
    adj = defaultdict(list)
    edge_info = dict()
    for (x, y, l, a) in edges:
        adj[x].append(y)
        adj[y].append(x)
        edge_info[(x, y)] = (l, a)
        edge_info[(y, x)] = (l, a)

    parents = bfs(adj, 1)

    toll_gcds = []

    @functools.lru_cache(maxsize=None)
    def get_road_info(i):
        if i == 1:
            return ([], [])
        else:
            lls, tcs = get_road_info(parents[i])
            ll, tc = edge_info[(i, parents[i])]
            ll_full, tc_full = zip(*sorted(zip(lls + [ll], tcs + [tc])))
            return (list(ll_full), list(tc_full))

    for c, w in queries:
        lls, tcs = get_road_info(c)
        i = bisect.bisect_right(lls, w)
        tolls = tcs[:i]
        # eprint(load_limits_to_capital[c])
        # eprint(toll_charges_to_capital[c])
        # eprint(i)
        # eprint(tolls)
        # eprint()
        if len(tolls) == 0:
            toll_gcd = 0
        else:
            toll_gcd = reduce(gcd, tolls)
        toll_gcds.append(toll_gcd)
    return " ".join(map(str, toll_gcds))


class setdeque(object):
    def __init__(self):
        self.q = deque()
        self.s = set()

    def __len__(self):
        return len(self.s)

    def add(self, a):
        self.q.append(a)
        self.s.add(a)

    def pop(self):
        v = self.q.popleft()
        self.s.remove(v)
        return v

    def contains(self, v):
        return v in self.s


def bfs(adj, v_source: int):
    # maps each node to its parent
    parents = dict()
    to_visit = setdeque()
    parents[v_source] = None
    to_visit.add(v_source)
    while len(to_visit) > 0:
        v = to_visit.pop()
        for u in adj[v]:
            if u in parents or to_visit.contains(u):
                continue
            to_visit.add(u)
            parents[u] = v
    return parents


## Comment out the appropriate option
# Option A: Multiple lines per case
num_cases = int(input())
for i in range(num_cases):
    n, q = get_vals(input())
    edges = []
    for _ in range(n - 1):
        edges.append(get_vals(input()))
    queries = []
    for _ in range(q):
        queries.append(get_vals(input()))
    print(f"Case #{i+1}: {process(edges, queries)}")
