import re

with open("data/day05_input.txt") as f:
    input = f.read().splitlines()

def parse_moves(input):
    moves = []
    digits_pattern = re.compile(r'(\d+)')
    for line in input:
        line_digits = [int(d) for d in digits_pattern.findall(line)]
        moves.append([(line_digits[i] if i == 0 else line_digits[i] - 1) for i in range(3)])
    return moves

MOVES = parse_moves(input)
STACKS = [
    ['Z', 'J', 'N', 'W', 'P', 'S'],
    ['G', 'S', 'T'],
    ['V', 'Q', 'R', 'L', 'H'],
    ['V', 'S', 'T', 'D'],
    ['Q', 'Z', 'T', 'D', 'B', 'M', 'J'],
    ['M', 'W', 'T', 'J', 'D', 'C', 'Z', 'L'],
    ['L', 'P', 'M', 'W', 'G', 'T', 'J'],
    ['N', 'G', 'M', 'T', 'B', 'F', 'Q', 'H'], ['R', 'D', 'G', 'C', 'P', 'B', 'Q', 'W']
]

############################################################

def day_5(stacks, moves, stack_move_order):
    stacks = stacks.copy()
    for [count, src, dest] in moves:
        stacks[dest] += stacks[src][-count:][::stack_move_order]
        stacks[src] = stacks[src][:-count]
    return ''.join([stack[-1] for stack in stacks if len(stack)])

print('Part 1: ', day_5(STACKS, MOVES, -1))
print('Part 2: ', day_5(STACKS, MOVES, 1))
