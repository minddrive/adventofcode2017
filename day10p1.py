#!/usr/bin/env python3

with open('input/day10.txt') as fh:
    lengths = [int(x) for x in fh.read().strip().split(',')]

circle = list(range(256))
curr_pos = 0
skip_size = 0

for length in lengths:
    for idx in range(length // 2):
        now = (curr_pos + idx) % len(circle)
        later = (curr_pos + length - 1 - idx) % len(circle)
        circle[now], circle[later] = circle[later], circle[now]

    curr_pos += length + skip_size
    skip_size += 1

print(circle[0] * circle[1])
