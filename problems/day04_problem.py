with open("data/day04_input.txt") as f:
    input = f.read().splitlines()

def is_contained(data, count_any_overlap = False):
    [x, y] = data.split(',')
    [x_start, x_end] = x.split('-')
    [y_start, y_end] = y.split('-')

    x_set = set(range(int(x_start), int(x_end) + 1))
    y_set = set(range(int(y_start), int(y_end) + 1))

    overlap = list(x_set & y_set)
    overlap_len = len(overlap)
    if count_any_overlap:
        return overlap_len > 0
    return overlap_len >= len(x_set) or overlap_len >= len(y_set)


def part_1(input):
    total = 0
    for row in input:
        if is_contained(row):
            total += 1
    return total

print('Part 1: ', part_1(input))

def part_2(input):
    total = 0
    for row in input:
        if is_contained(row, True):
            total += 1
    return total

print('Part 2: ', part_2(input))
