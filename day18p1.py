#!/usr/bin/env python3

from collections import defaultdict


regs = defaultdict(int)
instr_list = list()
instr_pos = 0
prev_snd = None


def get_val(val):
    try:
        return int(val)
    except ValueError:
        return regs[val]


with open('input/day18.txt') as fh:
    instrs = fh.read().strip().split('\n')

for instr in instrs:
    instr_list.append(instr.split())

while True:
    if instr_pos < 0 or instr_pos >= len(instr_list):
        break

    in_type, data = instr_list[instr_pos][0], instr_list[instr_pos][1:]

    if in_type == 'snd':
        prev_snd = get_val(data[0])
    elif in_type == 'set':
        reg, val = data
        regs[reg] = get_val(val)
    elif in_type == 'add':
        reg, val = data
        regs[reg] += get_val(val)
    elif in_type == 'mul':
        reg, val = data
        regs[reg] *= get_val(val)
    elif in_type == 'mod':
        reg, val = data
        regs[reg] %= get_val(val)
    elif in_type == 'rcv':
        reg = data[0]
        if regs[reg]:
            print(prev_snd)
            break
    elif in_type == 'jgz':
        reg, val = data
        if regs[reg]:
            instr_pos += get_val(val)
            continue

    instr_pos += 1
