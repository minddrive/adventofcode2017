#!/usr/bin/env python3

"""
Day 6 of the Advent Of Code 2017 challenge

See http://adventofcode.com/2017/day/6 for details
"""

from get_input import get_input


# Read in data as a list of integers
data = [int(val) for val in get_input().split()]


def get_num_of_cycles(buckets, loop_length=False):
    """
    Determine the number of cycles to redistribute the buckets until
    the same configuration is seen

    For a given set of buckets, find the largest (first in list wins
    when lengths are the same) and distribute all elements to each of
    the successive buckets one element at time, cycling around when
    reaching the end.  Continue this process until a previous
    configuration is seen

    Return the number of cycles done, or if 'loop_length' is True,
    just the number of cycles since the previous occurrence of the
    last cycle
    """

    cycles = 1
    configs = [buckets.copy()]

    while True:
        bucket = max(buckets)
        b_idx = buckets.index(bucket)
        buckets[b_idx] = 0

        for cnt in range(b_idx + 1, b_idx + bucket + 1):
            buckets[cnt % len(buckets)] += 1

        if buckets in configs:
            if loop_length:
                return cycles - configs.index(buckets)

            break

        cycles += 1
        configs.append(buckets.copy())

    return cycles


# Print solutions
dataset_one = data.copy()
print(f'Part 1: {get_num_of_cycles(dataset_one)}')
dataset_two = data.copy()
print(f'Part 2: {get_num_of_cycles(dataset_two, loop_length=True)}')
