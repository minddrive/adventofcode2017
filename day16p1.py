#!/usr/bin/env python3


progs = 'abcdefghijklmnop'

with open('input/day16.txt') as fh:
    moves = fh.read().strip().split(',')

for move in moves:
    if move.startswith('s'):
        num = int(move[1:])
        progs = progs[-num:] + progs[:-num]
    elif move.startswith('p'):
        first, second = move[1:].split('/')
        f_idx, s_idx = sorted([progs.index(first), progs.index(second)])
        progs = progs[:f_idx] + progs[s_idx] + \
                progs[f_idx+1:s_idx] + progs[f_idx] + progs[s_idx+1:]
    elif move.startswith('x'):
        first, second = sorted([int(x) for x in move[1:].split('/')])
        progs = progs[:first] + progs[second] + \
                progs[first+1:second] + progs[first] + progs[second+1:]

print(progs)
