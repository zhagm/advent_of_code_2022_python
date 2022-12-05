import re

with open("data/day05_input.txt") as f:
    input = f.read().splitlines()

def parse_data(input):
    stacks = [[] for i in range(10)]
    moves_start = -1
    for line_index in range(len(input)):
        line = input[line_index]
        stack_num = 0
        if (line[1] == '1'):
            moves_start = line_index + 2
            break
        for item in [line[i] for i in range(1, len(line), 4)]:
            stack_num += 1
            if item != ' ':
                stacks[stack_num].insert(0, item)
    moves = []
    digits_pattern = re.compile(r'(\d+)')
    for line in input[moves_start:]:
        moves.append([int(d) for d in digits_pattern.findall(line)])
    return stacks, moves

STACKS, MOVES = parse_data(input)

############################################################

def part_1(stacks, moves):
    for [count, src, dest] in moves:
        stacks[dest] = stacks[dest] + stacks[src][-count:][::-1]
        stacks[src] = stacks[src][:-count]
    return ''.join([stack[-1] for stack in stacks[1:] if len(stack)])

print('Part 1: ', part_1(STACKS.copy(), MOVES))

def part_2(stacks, moves):
    for [count, src, dest] in moves:
        stacks[dest] = stacks[dest] + stacks[src][-count:]
        stacks[src] = stacks[src][:-count]
    return ''.join([stack[-1] for stack in stacks[1:] if len(stack)])

print('Part 2: ', part_2(STACKS.copy(), MOVES))
