#!/usr/bin/env python3

"""
Day 3 of the Advent Of Code 2017 challenge

See http://adventofcode.com/2017/day/3 for details

Thanks for Ron Frederick for the algorithm for the manhattan distance
"""

from collections import defaultdict
from math import sqrt

from get_input import get_input


# Input is a single integer
val = int(get_input())


def manhattan_distance(num):
    """
    Calculate the shortest number of steps from a given integer in
    the spiral to the integer 1, using only left/right/up/down moves

    This is done by calculating what "ring" the number is in (the
    number 1 being the zeroth ring, 2 to 9 in the ring 1, 10 to 25
    in ring 2, etc), determining the position of the number in the
    determined ring, then determining the offset to get the number
    of steps
    """

    ring = int(sqrt(num - 1) + 1) // 2
    pos = (2 * ring + 1) ** 2 - num
    offset = pos % (2 * ring)

    return ring + abs(offset - ring)


def fill_cell(sums, num, pos_x, pos_y):
    """
    Determine the value for the current cell by adding all values in
    the cells around it (value 0 if the cell is empty).  Also determine
    if the value is greater that the given number

    Returns a tuple of the value in the cell and if it was larger than
    the given number or not
    """

    newnum = sum(
        sums.get((pos_x + i, pos_y + j), 0)
        for i in [-1, 0, 1] for j in [-1, 0, 1]
    )

    sums[(pos_x, pos_y)] = newnum
    found = True if newnum > num else False

    return newnum, found


def find_largest_sum(num):
    """
    For a given number, run through the spiral and create the proper
    sum for each given cell (total of all directly adjacent cells that
    have values), and return when the number in the current cell is
    greater than the given number
    """

    deltas = ((1, 0), (0, 1), (-1, 0), (0, -1))

    sums = defaultdict(int)
    sums[(0, 0)] = 1
    x, y = 0, 0
    direction = 0
    side = 0

    while True:
        dx, dy = deltas[direction]

        # The length of the side increases every other time
        for idx in range(side // 2 + 1):
            x += dx
            y += dy
            newnum, found = fill_cell(sums, num, x, y)

            if found:
                return newnum

        direction = (direction + 1) % 4
        side += 1


# Print solutions
print(f'Part 1: {manhattan_distance(val)}')
print(f'Part 2: {find_largest_sum(val)}')
