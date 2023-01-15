from math import prod
from copy import deepcopy

with open("data/day11_input.txt") as f:
    input = f.read().split('\n\n')

class Monkey:
    def __init__(self, items, operation, mod, t, f):
        self.items = items
        self.op = operation
        self.mod = mod
        self.true = t
        self.false = f
        self.inspect_count = 0
        self.mod_divs = 0
    
    def turn(self):
        self.inspect_count += len(self.items)
        for item in self.items:
            worry_level = self.op(item) // 3
            dest_monkey = self.true if worry_level % self.mod == 0 else self.false
            MONKEYS[dest_monkey].items.append(worry_level)
        self.items = []

    def turn2(self, lcm):
        self.inspect_count += len(self.items)
        for item in self.items:
            worry_level = self.op(item) % lcm
            dest_monkey = self.true if worry_level % self.mod == 0 else self.false
            MONKEYS[dest_monkey].items.append(worry_level)
        self.items = []

MONKEYS = [
    Monkey([92, 73, 86, 83, 65, 51, 55, 93], lambda x: x * 5, 11, 3, 4),
    Monkey([99, 67, 62, 61, 59, 98], lambda x: x * x, 2, 6, 7),
    Monkey([81, 89, 56, 61, 99], lambda x: x * 7, 5, 1, 5),
    Monkey([97, 74, 68], lambda x: x + 1, 17, 2, 5),
    Monkey([78, 73], lambda x: x + 3, 19, 2, 3),
    Monkey([50], lambda x: x + 5, 7, 1, 6),
    Monkey([95, 88, 53, 75], lambda x: x + 8, 3, 0, 7),
    Monkey([50, 77, 98, 85, 94, 56, 89], lambda x: x + 2, 13, 4, 0),
]
# MONKEYS = [
#     Monkey([79, 98], lambda x: x * 19, lambda x: 2 if x % 23 == 0 else 3),
#     Monkey([54, 65, 75, 74], lambda x: x + 6, lambda x: 2 if x % 19 == 0 else 0),
#     Monkey([79, 60, 97], lambda x: x * x, lambda x: 1 if x % 13 == 0 else 3),
#     Monkey([74], lambda x: x + 3, lambda x: 0 if x % 17 == 0 else 1),
# ]

def part_1(rounds, monkeys):
    for round in range(rounds):
        for m in monkeys:
            m.turn()
    maxes = [m.inspect_count for m in monkeys]
    maxes.sort()
    return maxes[-1] * maxes[-2]

def part_2(rounds, monkeys):
    lcm = prod([m.mod for m in monkeys])
    for round in range(rounds):
        for m in monkeys:
            m.turn2(lcm)
    maxes = [m.inspect_count for m in monkeys]
    maxes.sort()
    print(maxes, maxes[-1], maxes[-2])
    return maxes[-1] * maxes[-2]

print('Part 2: ', part_2(10000, MONKEYS))
# print('Part 1: ', part_1(20, MONKEYS))
