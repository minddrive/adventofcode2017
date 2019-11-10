#!/usr/bin/env python3

"""
Day 2 of the Advent Of Code 2017 challenge

See http://adventofcode.com/2017/day/2 for details
"""

from get_input import get_input


# Read in data as an array of string of a list of integers
data = get_input().split('\n')


def get_checkum(divides=False):
    """
    Calculate checksum, which depends on if 'divides' is set:

    If not, checksum is the sum of the differences of the biggest and
    smallest numbers of each row

    If so, checksum is the sum of the divisions of the two numbers
    that divide each other evenly in each line (only one pair)

    Returns the checksum
    """

    checksum = 0

    for row in data:
        nums = [int(x) for x in row.split()]

        if divides:
            # Figure out which two numbers have an "even" division,
            # and add the result to the checksum
            for f_idx in range(len(nums) - 1):
                for s_idx in range(f_idx + 1, len(nums)):
                    first, second = nums[f_idx], nums[s_idx]

                    if first % second == 0:
                        checksum += first // second
                        break
                    elif second % first == 0:
                        checksum += second // first
                        break
        else:
            # Find the max and min values and add the difference
            # to the checksum
            minval, maxval = nums[0], nums[0]

            for idx in range(1, len(nums)):
                if nums[idx] < minval:
                    minval = nums[idx]
                elif nums[idx] > maxval:
                    maxval = nums[idx]

            checksum += (maxval - minval)

    return checksum


# Print solutions
print(f'Part 1: {get_checkum()}')
print(f'Part 2: {get_checkum(divides=True)}')
