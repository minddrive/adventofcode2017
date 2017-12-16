#!/usr/bin/env python3

import operator
import sys

from functools import reduce


my_key = 'xlqgujun'


def rotate(l, pos):
    return l[pos:] + l[:pos]


class KnotHash:
    _circlen = 256

    def __init__(self, inp):
        self._circ = list(range(self._circlen))
        self._pos = 0
        self._skip = 0
        self._lengths = [ord(c) for c in inp] + [17,31,73,47,23]

    def _do_round(self):
        for l in self._lengths:
            self._circ = rotate(list(reversed(self._circ[:l])) + self._circ[l:],
                                (l + self._skip) % self._circlen)
            self._pos = (self._pos + l + self._skip) % self._circlen
            self._skip += 1

    def hash(self, rounds=64):
        for _ in range(rounds):
            self._do_round()

        if self._pos:
            self._circ = rotate(self._circ, self._circlen - self._pos)

        return [reduce(operator.xor, self._circ[p*16:(p+1)*16])
                    for p in range(16)]


grid = list()

for idx in range(128):
    hash = KnotHash(f'{my_key}-{idx}').hash()
    grid.append(list(''.join('{0:08b}'.format(h) for h in hash)))

squares = 0

for row in range(128):
    for col in range(128):
        if grid[row][col] == '1':
            squares += 1

print(squares)
