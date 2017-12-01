#!/usr/bin/env python3

with open('input/day01.txt') as fh:
    data = fh.read().strip()

numlen = len(data)
matches = list()

for idx in range(numlen):
    if data[idx] == data[(idx + 1) % numlen]:
        matches.append(int(data[idx]))

print(sum(matches))
