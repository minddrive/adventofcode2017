#!/usr/bin/env python3


def next_nums():
    A = 703
    B = 516

    for _ in range(40000000):
        A *= 16807
        A %= 2147483647
        B *= 48271
        B %= 2147483647
        yield (A, B)


count = 0

for newA, newB in next_nums():
    if newA % 65536 == newB % 65536:
        count += 1

print(count)
