#!/usr/bin/env python3

from math import sqrt

input = 277678

import itertools

nine_directions = list(itertools.product(range(-1, 1 + 1), range(-1, 1 + 1)))


def solve1(input_num):
    current_number = 1
    x = y = 0
    delta = 0

    four_directions = [(+1, 0), (0, +1), (-1, 0), (0, -1)]  # right up left down
    while current_number < input_num:
        n_i = 0
        for _ in range(2):
            for _ in range(2):
                for i in range(delta):
                    current_number += 1
                    direction = four_directions[n_i]
                    x += direction[0]
                    y += direction[1]
                    if current_number == input_num:
                        print("answer 1: ", abs(x) + abs(y))
                        return
                n_i += 1
            delta += 1


def solve2(input_num):
    def sum_adjacents(x, y):
        numbers[x][y] = sum(
            [numbers[x + n[0]][y + n[1]] for n in nine_directions])

    sq = int(input_num ** 0.5) + 1  # big enough
    numbers = [[0 for i in range(sq * 2)] for j in range(sq * 2)]

    current_number = 1
    x = y = sq
    numbers[x][y] = current_number
    delta = 0

    four_directions = [(+1, 0), (0, +1), (-1, 0), (0, -1)]  # right up left down
    while numbers[x][y] <= input_num:
        n_i = 0
        for _ in range(2):
            for _ in range(2):
                for i in range(delta):
                    current_number += 1
                    direction = four_directions[n_i]
                    x += direction[0]
                    y += direction[1]
                    sum_adjacents(x, y)
                    if numbers[x][y] > input_num:
                        print("answer 2: ", numbers[x][y])
                        return
                n_i += 1
            delta += 1


solve1(input)

