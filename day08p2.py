#!/usr/bin/env python3

from collections import defaultdict
from operator import eq, ge, gt, le, lt, ne, add, sub


ops = {'==': eq, '>=': ge, '>': gt, '<=': le, '<': lt, '!=': ne,
       'inc': add, 'dec': sub}
regs = defaultdict(int)
hp = -1000000000

with open('input/day08.txt') as fh:
    insts = fh.read().strip().split('\n')

for inst in insts:
    reg1, op1, num1, _, reg2, op2, num2 = inst.split()

    if ops[op2](regs[reg2], int(num2)):
        regs[reg1] = ops[op1](regs[reg1], int(num1))

    hp = max(hp, max(regs.values()))

print(hp)
