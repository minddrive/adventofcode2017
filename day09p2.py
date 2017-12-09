#!/usr/bin/env python3

with open('input/day09.txt') as fh:
    stream = fh.read().strip()

garbage = False
gchars = 0

idx = 0

while idx < len(stream):
    if stream[idx] == '!':
        idx += 1
    elif garbage:
        if stream[idx] == '>':
            garbage = False
        else:
            gchars += 1
    elif stream[idx] == '<':
        garbage = True

    idx += 1

print(gchars)
