#!/usr/bin/env python3


from collections import defaultdict


def get_vals(s):
    return list(map(int, s.strip().split()))


def add(t1, t2):
    return tuple([x + y for x, y in zip(t1, t2)])


DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def get_neighbors(t, r, c):
    for dir in DIRS:
        t_n = add(t, dir)
        if 0 <= t_n[0] < r and 0 <= t_n[1] < c:
            yield t_n


def process(cell_to_height, r, c):
    height_to_cells = defaultdict(set)
    for cell, height in cell_to_height.items():
        height_to_cells[height].add(cell)
    max_height = max(height_to_cells.keys())
    # current cell we are adding heights to the neighbors for
    cur_height = max_height
    total_boxes_added = 0
    while cur_height in height_to_cells:
        for cell in height_to_cells[cur_height]:
            for neighbor_cell in get_neighbors(cell, r, c):
                neighbor_cell_height = cell_to_height[neighbor_cell]
                boxes_needed = (cur_height - 1) - neighbor_cell_height
                if boxes_needed > 0:
                    # neighboring cell os shorter than the current cell by greater than 1
                    # add boxes until it is at cur_height - 1
                    total_boxes_added += boxes_needed
                    cell_to_height[neighbor_cell] = cur_height - 1
                    height_to_cells[neighbor_cell_height].remove(neighbor_cell)
                    height_to_cells[cur_height - 1].add(neighbor_cell)
        cur_height -= 1
    return total_boxes_added


## Comment out the appropriate option
# Option A: Multiple lines per case
num_cases = int(input())
for case_no in range(num_cases):
    r, c = get_vals(input())
    cell_to_height = dict()
    for i in range(r):
        for j, e in enumerate(get_vals(input())):
            cell_to_height[(i, j)] = e
    print(f"Case #{case_no+1}: {process(cell_to_height, r, c)}")
