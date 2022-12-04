with open("data/day04_input.txt") as f:
    input = f.read().splitlines()

class IntRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def parse_pair(pair):
    [[a_start, a_end], [b_start, b_end]] = [[int(x) for x in y.split('-')] for y in pair.split(',')]
    return IntRange(a_start, a_end), IntRange(b_start, b_end)

def part_1(input):
    total = 0
    for first, second in map(parse_pair, input):
        if (first.start >= second.start and first.end <= second.end) \
            or (second.start >= first.start and second.end <= first.end):
            total += 1
    return total

print('Part 1: ', part_1(input))

def part_2(input):
    total = 0
    for first, second in map(parse_pair, input):
        if (first.start >= second.start and first.end <= second.end) \
            or (second.start >= first.start and second.end <= first.end) \
            or (first.end >= second.start and first.end <= second.end) \
            or (second.end >= first.start and second.end <= first.end):
            total += 1
    return total

print('Part 2: ', part_2(input))
