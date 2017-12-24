#!/usr/bin/env python3

import time


count = 0
curr_pos = (0, 0)
prev_pos = None
dts = set([(-1, 0), (0, 1), (1, 0), (0, -1)])
curr_dt = None


def get_map_pos(pos):
    try:
        return map[pos[0]][pos[1]]
    except IndexError:
        return None


with open('input/day19.txt') as fh:
    map = [[ch for ch in line] for line in fh.read().split('\n')]

# Find entry point
first_line = map[0]

for idx in range(len(first_line)):
    if map[0][idx] != ' ':
        count += 1
        curr_pos = (0, idx)
        prev_pos = (-1, idx)
        curr_dt = (1, 0)
        break

while True:
    # Try moving in same direction
    next_pos = (curr_pos[0] + curr_dt[0], curr_pos[1] + curr_dt[1])
    char = get_map_pos(next_pos)

    if char is not None and char != ' ':
        prev_pos = curr_pos
        curr_pos = next_pos
        count += 1
        continue

    # Must have hit a turn, try other directions
    for dt in dts - set(curr_dt):
        next_pos = (curr_pos[0] + dt[0], curr_pos[1] + dt[1])

        if next_pos == prev_pos:
            continue

        char = get_map_pos(next_pos)

        if char is not None and char != ' ':
            prev_pos = curr_pos
            curr_pos = next_pos
            curr_dt = dt
            count += 1
            break
    else:
        print(count)
        break
