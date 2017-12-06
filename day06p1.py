#!/usr/bin/env python3

with open('input/day06.txt') as fh:
    buckets = [int(x) for x in fh.read().strip().split()]

cycles = 1
configs = [list(buckets)]

while True:
    bucket = max(buckets)
    b_idx = buckets.index(bucket)
    buckets[b_idx] = 0

    for cnt in range(b_idx + 1, b_idx + bucket + 1):
        buckets[cnt % len(buckets)] += 1

    if buckets in configs:
        break

    cycles += 1
    configs.append(list(buckets))

print(cycles)
