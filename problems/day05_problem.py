import re

with open("data/day05_input.txt") as f:
    input = f.read().splitlines()

def parse_moves(input):
    moves = []
    digits_pattern = re.compile(r'(\d+)')
    for line in input:
        moves.append([int(d) for d in digits_pattern.findall(line)])
    return moves

MOVES = parse_moves(input)
STACKS = [
    [],
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

def part_1(stacks, moves):
    stacks = stacks.copy()
    for [count, src, dest] in moves:
        stacks[dest] += stacks[src][-count:][::-1]
        stacks[src] = stacks[src][:-count]
    return ''.join([stack[-1] for stack in stacks if len(stack)])

print('Part 1: ', part_1(STACKS, MOVES))

def part_2(stacks, moves):
    stacks = stacks.copy()
    for [count, src, dest] in moves:
        stacks[dest] += stacks[src][-count:]
        stacks[src] = stacks[src][:-count]
    return ''.join([stack[-1] for stack in stacks if len(stack)])

print('Part 2: ', part_2(STACKS, MOVES))
