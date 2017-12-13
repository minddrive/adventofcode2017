#!/usr/bin/env python3


with open('input/day13.txt') as fh:
    layers = {int(x): int(y) for x, y in (z.split(': ')
                             for z in fh.read().strip().split('\n'))}

severity = 0
delay = 0
more = True


while more:
    for pos, length in layers.items():
        if (pos + delay) % ((length - 1) * 2) == 0:
            break
    else:
        more = False
        break

    delay += 1

print(delay)
