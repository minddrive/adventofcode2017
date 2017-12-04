#!/usr/bin/env python3

with open('input/day04.txt') as fh:
    data = fh.read().strip().split('\n')

unique = 0
for line in data:
    words = [''.join(sorted(word)) for word in line.split()]
    if sorted(words) == sorted(list(set(words))):
        unique += 1

print(unique)
