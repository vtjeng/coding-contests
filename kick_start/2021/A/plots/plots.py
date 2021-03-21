#!/usr/bin/env python3


from collections import defaultdict
import itertools
from typing import List, Tuple
import bisect


def get_vals(s):
    return list(map(int, s.strip().split()))


DIR_TO_VECTOR = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}


# def dir_to_vector(dir):
#     return DIR_TO_VECTOR[dir % 4]


def add(t1, t2):
    return tuple([x + y for x, y in zip(t1, t2)])


def count_num_ls(l1, l2):
    if l1 == 1 or l2 == 1:
        return 0
    l1_eff = min(l1, l2 // 2)
    l2_eff = min(l2, l1 // 2)
    return (l1_eff - 1) + (l2_eff - 1)


# def process(occupied_cells):
#     num_ls = 0
#     for cell in sorted(occupied_cells):
#         lengths = dict()
#         for dir, vector in DIR_TO_VECTOR.items():
#             cur_cell = cell
#             # includes cell at origin
#             length = 0
#             while cur_cell in occupied_cells:
#                 cur_cell = add(cur_cell, vector)
#                 length += 1
#             lengths[dir] = length
#         for i in range(4):
#             num_ls += count_num_ls(lengths[i % 4], lengths[(i + 1) % 4])
#         # print(f"cell: {cell}, lengths: {lengths}, num_ls: {num_ls}")
#     return num_ls


def get_block_info(occupied_cells: List[int]):
    assert len(occupied_cells) > 0
    prev_cell = None
    count = 0
    end_cells = []
    lengths = []
    for cell in occupied_cells:
        if prev_cell is None or cell == prev_cell + 1:
            count += 1
        else:
            # there's a gap
            end_cells.append(prev_cell)
            lengths.append(count)
            count = 1
        prev_cell = cell
    end_cells.append(prev_cell)
    lengths.append(count)
    # print(occupied_cells, end_cells, lengths, "")
    return end_cells, lengths


def find_arm_lengths(block_info: Tuple[List[int], List[int]], cell: int):
    end_cells, lengths = block_info
    i = bisect.bisect_left(end_cells, cell)
    end_cell = end_cells[i]
    length = lengths[i]
    start_cell = end_cell - length + 1
    back_arm_length = (cell - start_cell) + 1
    front_arm_length = (end_cell - cell) + 1
    return back_arm_length, front_arm_length


def process(occupied_cells, row_occupied_cells, col_occupied_cells):
    row_infos = dict()  # {row_id: ([block_end_col, ...], [block_length, ...])
    col_infos = dict()  # {col_id: ([block_end_row, ...], [block_length, ...])}
    for row_id, occupied_columns in row_occupied_cells.items():
        row_infos[row_id] = get_block_info(occupied_columns)
    for col_id, occupied_rows in col_occupied_cells.items():
        col_infos[col_id] = get_block_info(occupied_rows)

    num_ls = 0
    for cell in sorted(occupied_cells):
        i, j = cell
        arm_lengths = (
            find_arm_lengths(row_infos[i], j),
            find_arm_lengths(col_infos[j], i),
        )
        # print(f"cell: {cell}, arm_lengths: {arm_lengths}")
        for l1, l2 in itertools.product(*arm_lengths):
            # print(f"{l1}, {l2}")
            num_ls += count_num_ls(l1, l2)
        # print(f"cell: {cell}, lengths: {lengths}, num_ls: {num_ls}")
    return num_ls


## Comment out the appropriate option
# Option A: Multiple lines per case
num_cases = int(input())
for case_no in range(num_cases):
    r, c = get_vals(input())
    occupied_cells = set()
    row_occupied_cells = defaultdict(list)
    col_occupied_cells = defaultdict(list)
    for i in range(r):
        for j, e in enumerate(get_vals(input())):
            if e == 1:
                occupied_cells.add((i, j))
                row_occupied_cells[i].append(j)
                col_occupied_cells[j].append(i)
    print(
        f"Case #{case_no+1}: {process(occupied_cells, row_occupied_cells, col_occupied_cells)}"
    )
