#!/usr/bin/env python3


from collections import defaultdict
import heapq
from functools import lru_cache


def get_vals(s):
    return list(map(int, s.strip().split()))


# def get_dist(d_adj):
#     # https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
#     dist = defaultdict(lambda: float("inf"))
#     dist.update(d_adj)
#     vertices = set()
#     for edge in d_adj:
#         u, v = edge
#         vertices.add(u)
#         vertices.add(v)
#     for v in vertices:
#         dist[(v, v)] = 0
#     for k in vertices:
#         for i in vertices:
#             for j in vertices:
#                 dist[(i, j)] = min(dist[(i, j)], dist[(i, k)] + dist[(k, j)])

#     return dist


def process(room_colors, turbolifts, soldiers):
    # map of time to travel between rooms of different colors via turbolifts
    d_adj = defaultdict(lambda: float("inf"))

    def get_room_color(room_id):
        return room_colors[room_id - 1]

    for c in set(room_colors):
        d_adj[(c, c)] = 0

    for turbolift in turbolifts:
        room_a, room_b, time = turbolift
        c_a, c_b = map(get_room_color, (room_a, room_b))
        d_adj[(c_a, c_b)] = min(d_adj[(c_a, c_b)], time)

    neighbors = defaultdict(list)
    for edge in d_adj:
        u, v = edge
        neighbors[u].append(v)

    def get_dist(v_start, v_end):
        # not sure whether this optimization is necessary; this simply enables
        # us to avoid re-computing the shortest path from a given source
        return get_dists(v_start)[v_end]

    @lru_cache(maxsize=None)
    def get_dists(v_start):
        # Dijkstra's: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
        dist = defaultdict(lambda: float("inf"))
        q = set(room_colors)
        dist[v_start] = 0
        while len(q) > 0:
            u = min(q, key=lambda v: dist[v])
            # print(u)
            q.remove(u)

            for v in neighbors[u]:
                alt = dist[u] + d_adj[(u, v)]
                if alt < dist[v]:
                    dist[v] = alt
        # print(v_start, dist)
        return dist

    for soldier in soldiers:
        room_p, room_q = soldier
        c_p, c_q = map(get_room_color, (room_p, room_q))
        d = get_dist(c_p, c_q)
        if d == float("inf"):
            print(-1)
        else:
            print(d)


## Comment out the appropriate option
# Option A: Multiple lines per case
num_cases = int(input())
for i in range(num_cases):
    n = int(input())
    room_colors = [input() for _ in range(n)]
    m = int(input())
    turbolifts = [get_vals(input()) for _ in range(m)]
    s = int(input())
    soldiers = [get_vals(input()) for _ in range(s)]
    print(f"Case #{i+1}:")
    process(room_colors, turbolifts, soldiers)
