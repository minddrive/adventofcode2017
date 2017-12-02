#!/usr/bin/env python3

with open('input/day02.txt') as fh:
    data = fh.read().strip().split('\n')

sum = 0
for line in data:
    nums = sorted([int(x) for x in line.split()])
    sum += (nums[-1] - nums[0])

print(sum)
