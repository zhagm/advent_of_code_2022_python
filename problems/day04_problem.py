with open("data/day04_input.txt") as f:
    input = f.read().splitlines()

class IntRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def contains(self, other):
        return other.start >= self.start and other.end <= self.end

    def has_overlap(self, other):
        return self.end >= other.start and self.end <= other.end


def parse_pair(pair):
    [[a_start, a_end], [b_start, b_end]] = [[int(x) for x in y.split('-')] for y in pair.split(',')]
    return IntRange(a_start, a_end), IntRange(b_start, b_end)

def day_4(input, contained_overlaps_only = True):
    total = 0
    for first, second in map(parse_pair, input):
        if first.has_overlap(second) or second.has_overlap(first):
            if contained_overlaps_only:
                if (first.contains(second) or second.contains(first)):
                    total += 1
            else:
                total += 1
    return total

print('Part 1: ', day_4(input))
print('Part 2: ', day_4(input, False))
