#!/usr/bin/env python3


def get_vals(s):
    return list(map(int, s.strip().split()))


# numbers increase clockwise
DIR_TO_VECTOR = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
DIR_TO_CARD = {0: "N", 1: "E", 2: "S", 3: "W"}
STEP_THRESHOLD = 10000


def dir_to_vector(dir):
    return DIR_TO_VECTOR[dir % 4]


def dir_to_card(dir):
    return DIR_TO_CARD[dir % 4]


def add(t1, t2):
    return tuple([x + y for x, y in zip(t1, t2)])


def get_starting_direction(sx, sy):
    if sx == 0 and sy == 0:
        # starting at top left
        return 1
    if sx == 0:
        # starting at top right
        return 2
    if sy == 0:
        # starting at bottom left
        return 0
    # starting at bottom right
    return 3


def process(maze, pose):
    sx, sy, ex, ey = list(map(lambda x: x - 1, get_vals(pose)))
    end_pos = (ex, ey)

    ## maze is guaranteed square
    # n = len(maze)

    # set of all cells that are free
    free_cells = set()
    for r, row in enumerate(maze):
        for c, entry in enumerate(row):
            if entry == ".":
                free_cells.add((r, c))

    cur_dir = get_starting_direction(sx, sy)
    cur_pos = (sx, sy)
    # wall is on your LEFT hand, and we've defined
    cur_wall = add(cur_pos, dir_to_vector(cur_dir - 1))
    steps = []
    # visited_pozes tracks positions and directions
    visited_pozes = set()
    while cur_pos != end_pos:
        next_pos_candidate = add(cur_pos, dir_to_vector(cur_dir))
        if next_pos_candidate in free_cells:
            # can move in this direction
            cur_pos = next_pos_candidate
            steps.append(cur_dir)
            if len(steps) > STEP_THRESHOLD:
                return "Edison ran out of energy."
            # check if there is a wall to the left of the robot's current position (in the direction they are facing)
            # if there is, their direction remains the same
            if (add(cur_pos, dir_to_vector(cur_dir - 1))) in free_cells:
                # otherwise, the robot will turn counterclockwise to stay in touch with the wall
                cur_dir = (cur_dir - 1) % 4
        else:
            # can't move in the direction the robot is facing; there's a wall there
            # robot turns clockwise
            cur_dir = (cur_dir + 1) % 4
            cur_poze = cur_pos, cur_dir
            if cur_poze in visited_pozes:
                return "Edison ran out of energy."
            else:
                visited_pozes.add(cur_poze)
    return f"{len(steps)}\n" + "".join(map(dir_to_card, steps))


## Comment out the appropriate option
# Option A: Multiple lines per case
num_cases = int(input())
for i in range(num_cases):
    num_case_lines = int(input())
    maze = []
    for j in range(num_case_lines):
        maze.append(input())
    pose = input()
    print(f"Case #{i+1}: {process(maze, pose)}")
