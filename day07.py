#!/usr/bin/env python3

"""
Day 7 of the Advent Of Code 2017 challenge

See http://adventofcode.com/2017/day/7 for details

Many thanks to Ron Frederick for the balance algorithm
"""

import sys

from collections import Counter, defaultdict

from get_input import get_input


# Read in data as a list of strings
data = get_input().split('\n')


class Program:
    """
    Basic class representing a given 'program' in the tower

    Includes method to determine unbalanced program within the tower
    """

    def __init__(self, name, weight, children):
        """
        Basic initialization, including tracking the parent and total
        weight for the sub-tower under the given program
        """

        self.name = name
        self.weight = weight
        self.children = children
        self.parent = None
        self.total_weight = 0

    def balance(self):
        """
        Determine the unbalanced program and return the corrected value
        needed to balance the tower

        The tree is travelled until it finds the topmost part of the
        unbalance, then sorts the weights and compares to determine
        the difference needed, then calculates the correct weight
        """

        for child in self.children:
            found, val = child.balance()

            if found:
                return found, val

        # Sort children from heaviest to lightest
        children = sorted(self.children,
                          key=lambda child: -child.total_weight)

        # If there's more than one child (needed for imbalance),
        # compare the weights of the heaviest and lightest; if they
        # don't match, take the difference between the two and
        # remove it from the heaviest weight to determine the
        # correct weight.  Note this works regardless of whether
        # the invalid weight is lighter or heavier.
        if len(children) > 1:
            weight0 = children[0].total_weight
            weight1 = children[-1].total_weight

            if weight0 != weight1:
                return True, children[0].weight - (weight0 - weight1)

        # Calculate total weight to use for further checking up
        # the tree
        self.total_weight = self.weight + sum(child.total_weight
                                              for child in self.children)

        return False, 0


def generate_tree_info():
    """
    Create tower based on data given for each program, replacing
    list of children names in every program with the actual children
    (generated from Program class)
    """

    prog_info = dict()

    for prog_data in data:
        prog, weight, *children = prog_data.replace(',', '').split()
        prog_info[prog] = Program(
            prog,
            int(weight[1:-1]),  # Remove parentheses
            children[1:]  # Remove '->'
        )

    for prog in prog_info.values():
        prog.children = [prog_info[child] for child in prog.children]
        for child in prog.children:
            child.parent = prog.name

    return prog_info


def find_root(prog_info):
    """
    Determine the base of the tower (it will be the only program
    without a parent)
    """

    return [prog for prog in prog_info.values() if prog.parent is None][0]


# Print solutions
info = generate_tree_info()
root = find_root(info)
print(f'Part 1: {root.name}')
print(f'Part 2: {root.balance()[1]}')
