with open("input.txt") as f:
    input = f.read()

def part_1(input):
    lines = input.splitlines()
    for i in range(len(lines)):
        lines[i] = int(lines[i]) if lines[i] else lines[i]
    max = 0
    curr = 0
    for item in lines:
        if item == '':
            if curr > max:
                max = curr
            curr = 0
        else:
            curr = curr + item
    return max

print('Part 1: ', part_1(input))


def first_try_2(input):
    groups = input.split('\n\n')
    totals = []
    for group in groups:
        total = sum([int(item) for item in group.split('\n')])
        totals.append(total)
    totals.sort()
    return sum(totals[-3:])

print('Part 2: ', part_2(input))
