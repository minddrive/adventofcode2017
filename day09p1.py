#!/usr/bin/env python3

with open('input/day09.txt') as fh:
    stream = fh.read().strip()

points = 0
curr_point = 0
garbage = False

idx = 0

while idx < len(stream):
    if stream[idx] == '!':
        idx += 1
    elif garbage:
        if stream[idx] == '>':
            garbage = False
    elif stream[idx] == '{':
        curr_point += 1
    elif stream[idx] == '<':
        garbage = True
    elif stream[idx] == '}':
        points += curr_point
        curr_point -= 1

    idx += 1

print(points)
