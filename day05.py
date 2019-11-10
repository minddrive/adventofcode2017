#!/usr/bin/env python3

"""
Day 5 of the Advent Of Code 2017 challenge

See http://adventofcode.com/2017/day/5 for details
"""

from get_input import get_input


# Read in data as a list of integers
initial_data = [int(val) for val in get_input().split('\n')]


def get_steps_to_exit(data, strange=False):
    """
    Determine the number of steps to exit the 'maze'

    Starting at the first element, move the number of steps based on
    the value of the current element, and either bump it by one, or
    if 'strange' is True and the value is over three, decrease it by
    one.  If the new position is outside the current list of elements,
    we can exit

    Returns the number of steps it takes to exit
    """

    jumps = 0
    idx = 0

    while 0 <= idx < len(data):
        new_idx = idx + data[idx]

        if strange and data[idx] >= 3:
            data[idx] -= 1
        else:
            data[idx] += 1

        jumps += 1
        idx = new_idx

    return jumps


# Print solutions
dataset_one = initial_data.copy()
print(f'Part 1: {get_steps_to_exit(dataset_one)}')
dataset_two = initial_data.copy()
print(f'Part 2: {get_steps_to_exit(dataset_two, strange=True)}')
