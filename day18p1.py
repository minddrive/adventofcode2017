#!/usr/bin/env python3

steps = 316
circ_buffer = [0]
pos = 0

for cnt in range(1, 2018):
    pos = (pos + steps) % cnt
    circ_buffer.insert(pos + 1, cnt)
    pos += 1

print(circ_buffer[pos + 1])
