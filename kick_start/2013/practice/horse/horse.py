#!/usr/bin/env python3

# import networkx as nx
# from networkx.algorithms import bipartite
from collections import defaultdict


def is_bipartite(adj):
    # check if graph is bipartite
    # per https://math.stackexchange.com/questions/310092/the-two-clique-problem-is-in-p-or-np-p-np-for-hypothesis
    # visited = set()
    boundary = set()
    unvisited = set(adj.keys())
    is_white = dict()
    while len(unvisited) > 0 or len(boundary) > 0:
        if len(boundary) == 0:
            v = unvisited.pop()
            is_white[v] = True
        else:
            v = boundary.pop()
        # visited.add(v)
        for u in adj[v]:
            if u in is_white:
                # either visited or on the boundary
                if is_white[u] == is_white[v]:
                    # an odd cycle exists
                    return False
            else:
                # currently unvisited; set to the opposite color
                is_white[u] = not is_white[v]
                unvisited.remove(u)
                boundary.add(u)
    return True


def process(case):
    adj = defaultdict(list)
    for pair in case:
        v1, v2 = pair.split()
        adj[v1].append(v2)
        adj[v2].append(v1)
    if is_bipartite(adj):
        return "Yes"
    else:
        return "No"
    # G = nx.Graph()
    # for pair in case:
    #     G.add_edge(*pair.split())
    # if bipartite.is_bipartite(G):
    #     return "Yes"
    # else:
    #     return "No"


num_cases = int(input())
for i in range(num_cases):
    num_case_lines = int(input())
    case = []
    for j in range(num_case_lines):
        case.append(input())
    print(f"Case #{i+1}: {process(case)}")
