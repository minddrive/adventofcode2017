#!/usr/bin/env python3

directions = {
    'n': (0, 2),
    's': (0, -2),
    'ne': (1, 1),
    'nw': (-1, 1),
    'se': (1, -1),
    'sw': (-1, -1),
}


def dist(x, y):
    return abs(x // 2) + abs(y // 2)


with open('input/day11.txt') as fh:
    steps = fh.read().strip().split(',')

curr_pos = [0, 0]
max_dist = 0

for step in steps:
    curr_pos[0] += directions[step][0]
    curr_pos[1] += directions[step][1]
    new_dist = dist(curr_pos[0], curr_pos[1])

    if new_dist > max_dist:
        max_dist = new_dist

print(max_dist)
