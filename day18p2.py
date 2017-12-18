#!/usr/bin/env python3

import queue

from collections import defaultdict


regs = [defaultdict(int), defaultdict(int)]
regs[1]['p'] = 1
queues = [queue.Queue(), queue.Queue()]
instr_list = list()
instr_pos = [0, 0]
states = ['ok', 'ok']


def get_val(prog, val):
    try:
        return int(val)
    except ValueError:
        return regs[prog][val]


with open('input/day18.txt') as fh:
    instrs = fh.read().strip().split('\n')

for instr in instrs:
    instr_list.append(instr.split())

prog = 0
count = 0

while True:
    in_type, data = instr_list[instr_pos[prog]][0], instr_list[instr_pos[prog]][1:]
    #print(prog, instr_pos[prog], in_type, data, queues[prog].qsize())

    if in_type == 'snd':
        queues[(prog + 1) % 2].put(get_val(prog, data[0]))
        if prog == 1:
            count += 1
    elif in_type == 'set':
        reg, val = data
        regs[prog][reg] = get_val(prog, val)
    elif in_type == 'add':
        reg, val = data
        regs[prog][reg] += get_val(prog, val)
    elif in_type == 'mul':
        reg, val = data
        regs[prog][reg] *= get_val(prog, val)
    elif in_type == 'mod':
        reg, val = data
        regs[prog][reg] %= get_val(prog, val)
    elif in_type == 'rcv':
        reg = data[0]
        if queues[prog].empty():
            if states[(prog + 1) % 2] == 'done':
                break
            if queues[(prog + 1) % 2].empty() and states[(prog + 1) % 2] == 'recv':
                break
            states[prog] = 'recv'
            prog = (prog + 1) % 2
        else:
            states[prog] = 'ok'
            regs[prog][reg] = queues[prog].get()
    elif in_type == 'jgz':
        reg, val = data
        if regs[prog][reg]:
            instr_pos[prog] += get_val(prog, val)

    instr_pos[prog] += 1

    if not 0 <= instr_pos[prog] < len(instr_list):
        if states[(prog + 1) % 2] == 'done':
            break
        else:
            states[prog] = 'done'
            prog = (prog + 1) % 2
            continue

print(count)
