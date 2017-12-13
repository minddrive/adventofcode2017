#!/usr/bin/env python3


with open('input/day13.txt') as fh:
    layers = {int(x): int(y) for x, y in (z.split(': ')
                             for z in fh.read().strip().split('\n'))}

severity = 0

for pos, length in layers.items():
    if pos % ((length - 1) * 2) == 0:
        severity += pos * length

print(severity)
