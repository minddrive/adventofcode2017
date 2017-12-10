#!/usr/bin/env python3

from functools import reduce
from operator import xor


with open('input/day10.txt') as fh:
    lengths = [ord(x) for x in fh.read().strip()] + [17, 31, 73, 47, 23]

circle = list(range(256))
curr_pos = 0
skip_size = 0

for loop in range(64):
    for length in lengths:
        for idx in range(length // 2):
            now = (curr_pos + idx) % len(circle)
            later = (curr_pos + length - 1 - idx) % len(circle)
            circle[now], circle[later] = circle[later], circle[now]

        curr_pos += length + skip_size
        skip_size += 1

hash = ''

for idx in range(16):
    hash += str(hex(reduce(xor, circle[16 * idx:16 * (idx + 1)]))[2:].zfill(2))

print(hash)
