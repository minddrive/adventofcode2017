#!/usr/bin/env python3

with open('input/day02.txt') as fh:
    data = fh.read().strip().split('\n')

sum = 0
for line in data:
    nums = sorted([int(x) for x in line.split()])
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] % nums[j] == 0:
                sum += (nums[i] // nums[j])
            elif nums[j] % nums[i] == 0:
                sum += (nums[j] // nums[i])

print(sum)
