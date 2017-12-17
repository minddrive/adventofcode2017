#!/usr/bin/env python3

steps = 316
circ_buffer = [0]
pos = 0
num = 0

for cnt in range(1, 50000001):
    pos = (pos + steps) % cnt

    if pos == 0:
        num = cnt

    pos += 1

print(num)
