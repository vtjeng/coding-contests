#!/usr/bin/env python3


from collections import defaultdict
import bisect


def get_vals(s):
    return list(map(int, s.strip().split()))


def process(missing_cells, missing_cols_in_row, missing_rows_in_col, costs):
    def remove(cell):
        missing_cells.remove(cell)
        i, j = cell
        missing_cols_in_row[i].remove(j)
        missing_rows_in_col[j].remove(i)

    def simplify():
        prev_num_cells_removed = -1
        cells_removed = []
        while len(cells_removed) > prev_num_cells_removed:
            prev_num_cells_removed = len(cells_removed)
            for row_id in set(missing_cols_in_row):
                col_ids = missing_cols_in_row[row_id]
                if len(col_ids) == 1:
                    i, j = row_id, list(col_ids)[0]
                    remove((i, j))
                    # missing_cells.remove((i, j))
                    # missing_rows_in_col[j].remove(i)
                    cells_removed.append((i, j))
                # this is a performance improvement
                if len(col_ids) <= 1:
                    del missing_cols_in_row[row_id]
            for col_id in set(missing_rows_in_col):
                row_ids = missing_rows_in_col[col_id]
                if len(row_ids) == 1:
                    i, j = list(row_ids)[0], col_id
                    remove((i, j))
                    # missing_cells.remove((i, j))
                    # missing_cols_in_row[i].remove(j)
                    cells_removed.append((i, j))
                if len(row_ids) <= 1:
                    del missing_rows_in_col[col_id]
        return cells_removed

    def restore(cells_removed):
        for cell in cells_removed:
            missing_cells.add(cell)
            i, j = cell
            missing_cols_in_row[i].add(j)
            missing_rows_in_col[j].add(i)

    simplify()
    # print(missing_cells, missing_rows_in_col, missing_cols_in_row)
    if len(missing_cells) == 0:
        return 0
    # these two lists will be the same length
    paid_cells_by_step = []  # List[Tuple[int, int]]
    cells_removed_by_step = []  # List[List[Tuple[int, int]]]
    cost_by_step = []

    # class Step(object):
    #     def __init__(self, cell):
    #         self.cell = cell

    #     def __enter__(self):
    #         cost_by_step.append(costs[self.cell[0]][self.cell[1]])
    #         paid_cells_by_step.append(self.cell)
    #         remove(self.cell)
    #         cells_removed_by_step.append(simplify() + [self.cell])

    #     def __exit__(self):
    #         restore(cells_removed_by_step.pop())
    #         paid_cells_by_step.pop()
    #         cost_by_step.pop()

    def recurse(candidate_cells, min_cost_so_far=float("inf")):
        min_cost = min_cost_so_far
        for i, cell in enumerate(candidate_cells):
            if cell not in missing_cells:
                continue
            cost_by_step.append(costs[cell[0]][cell[1]])
            if sum(cost_by_step) > min_cost:
                cost_by_step.pop()
                continue
            paid_cells_by_step.append(cell)
            # actually remove the cell you paid for
            remove(cell)
            cells_removed_by_step.append(simplify() + [cell])
            # print(f"{paid_cells_by_step}, {cells_removed_by_step}")
            if len(missing_cells) == 0:
                # we've removed a sequence of cells that allowed us to remove all cells
                min_cost = min(min_cost, sum(cost_by_step))
            else:
                min_cost = min(
                    min_cost, recurse(candidate_cells[i + 1 :], min_cost_so_far),
                )
            restore(cells_removed_by_step.pop())  # [[1, 0, 1]]
            paid_cells_by_step.pop()  # [[0, 0, 1]]
            cost_by_step.pop()
        return min_cost

    return recurse(sorted(missing_cells, key=lambda x: costs[x[0]][x[1]]))


## Comment out the appropriate option
# Option A: Multiple lines per case
num_cases = int(input())
for case_id in range(num_cases):
    n = int(input())
    missing_cells = set()
    # missing_cols_in_row[row_id] contains ids of columns that have -1 in A'
    missing_cols_in_row = defaultdict(set)
    missing_rows_in_col = defaultdict(set)
    costs = []
    for i in range(n):
        for j, e in enumerate(get_vals(input())):
            if e == -1:
                missing_cells.add((i, j))
                missing_cols_in_row[i].add(j)
                missing_rows_in_col[j].add(i)
    for i in range(n):
        costs.append(get_vals(input()))
    # row checksums
    input()
    # column checksums
    input()
    print(
        f"Case #{case_id+1}: {process(missing_cells, missing_cols_in_row, missing_rows_in_col, costs)}"
    )
