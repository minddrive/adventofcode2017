#!/usr/bin/env python3

"""
Day 1 of the Advent Of Code 2017 challenge

See http://adventofcode.com/2017/day/1 for details
"""

from get_input import get_input


# Read in data as a single string
data = get_input()

# Get length of numerical string and 'half' length (it's always even)
dlen = len(data)
half = dlen // 2


def get_sum(halfway=False):
    """
    Determine sum of digits consisting of either matching consecutive ones
    or ones "halfway" through the string (allowing for wrap-around) based
    on the part

    Returns the sum
    """

    digit_sum = 0
    offset = dlen // 2 if halfway else 1

    for idx in range(dlen):
        # If the "next" digit matches, add to sum
        if data[idx] == data[(idx + offset) % dlen]:
            digit_sum += int(data[idx])

    return digit_sum


# Print solutions
print(f'Part 1: {get_sum()}')
print(f'Part 2: {get_sum(halfway=True)}')
