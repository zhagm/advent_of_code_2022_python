with open("data/day11_input.txt") as f:
    input = f.read().split('\n\n')

class Monkey:
    def __init__(self, items, operation, test):
        self.items = items
        self.op = operation
        self.test = test
        self.inspect_count = 0
    
    def turn(self):
        self.inspect_count += len(self.items)
        for item in self.items:
            worry_level = self.op(item) // 3
            dest_monkey = self.test(worry_level)
            MONKEYS[dest_monkey].items.append(worry_level)
        self.items = []

MONKEYS = [
    Monkey([92, 73, 86, 83, 65, 51, 55, 93], lambda x: x * 5, lambda x: 3 if x % 11 == 0 else 4),
    Monkey([99, 67, 62, 61, 59, 98], lambda x: x * x, lambda x: 6 if x % 2 == 0 else 7),
    Monkey([81, 89, 56, 61, 99], lambda x: x * 7, lambda x: 1 if x % 5 == 0 else 5),
    Monkey([97, 74, 68], lambda x: x + 1, lambda x: 2 if x % 17 == 0 else 5),
    Monkey([78, 73], lambda x: x + 3, lambda x: 2 if x % 19 == 0 else 3),
    Monkey([50], lambda x: x + 5, lambda x: 1 if x % 7 == 0 else 6),
    Monkey([95, 88, 53, 75], lambda x: x + 8, lambda x: 0 if x % 3 == 0 else 7),
    Monkey([50, 77, 98, 85, 94, 56, 89], lambda x: x + 2, lambda x: 4 if x % 13 == 0 else 0),
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

print('Part 1: ', part_1(20, MONKEYS))
