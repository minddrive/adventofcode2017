#!/usr/bin/env python3


def find_group(seed):
    group = {seed}
    new = {seed}

    while new:
        next_new = set()

        for item in new:
            next_new.update(progs[item])

        new = next_new - group
        group.update(next_new)

    return group


def find_all_groups(nodes):
    remain = set(nodes.keys())
    groups = list()

    while remain:
        group = find_group(remain.pop())
        groups.append(group)
        remain -= group

    return groups


progs = dict()

with open('input/day12.txt') as fh:
    pipes = fh.read().strip().split('\n')

for pipe in pipes:
    src_prog, _, dest_progs = pipe.split(maxsplit=2)
    progs[src_prog] = dest_progs.split(', ')

print(len(find_all_groups(progs)))
