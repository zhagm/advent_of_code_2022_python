with open("data/day01_input.txt") as f:
    input = f.read()

def part_1(input):
    groups = input.split('\n\n')
    for group in groups:
        total = sum([int(item) for item in group.split('\n')])
        if total > max:
            max = total
    return max

print('Part 1: ', part_1(input))


def part_2(input):
    groups = input.split('\n\n')
    totals = []
    for group in groups:
        total = sum([int(item) for item in group.split('\n')])
        totals.append(total)
    totals.sort()
    return sum(totals[-3:])

print('Part 2: ', part_2(input))
