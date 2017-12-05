#!/usr/bin/env python3

with open('input/day05.txt') as fh:
    data = [int(x) for x in fh.read().strip().split('\n')]

jumps = 0
idx = 0

while idx >= 0 and idx < len(data):
    new_idx = idx + data[idx]
    data[idx] += 1
    jumps += 1
    idx = new_idx

print(jumps)
