#!/usr/bin/env python3

"""
Day 4 of the Advent Of Code 2017 challenge

See http://adventofcode.com/2017/day/4 for details
"""

from get_input import get_input


# Read in data as a list of strings
data = get_input().split('\n')


def get_unique(rearrange=False):
    """
    Determine the number of unique passphrases in a list

    For each passphrase, determine if the number of words in the phrase
    equals the number of unique words, and count that as unique if so;
    if the 'rearrange' parameter is True, also ensure none of the words
    can be rearranged to match others in the passphrase

    Returns the number of unique passphrases
    """

    unique = 0

    for line in data:
        words = line.split()

        if rearrange:
            words = [''.join(sorted(word)) for word in words]

        if sorted(words) == sorted(list(set(words))):
            unique += 1

    return unique


# Print solutions
print(f'Part 1: {get_unique()}')
print(f'Part 2: {get_unique(rearrange=True)}')
