with open("data/day03_input.txt") as f:
    input = f.read().splitlines()

def get_priority(c):
    charCode = ord(c)
    if charCode >= 65 and charCode <= 90:
        return charCode - 38
    if charCode >= 97 and charCode <= 122:
        return charCode - 96

def part_1(rucksacks):
    priority_sum = 0
    for r in rucksacks:
        half_len = len(r)//2
        first, second = r[:half_len], r[half_len:]
        duplicate = [item for item in first if second.find(item) != -1]
        priority_sum = priority_sum + get_priority(duplicate[0])
    return priority_sum

print('Part 1: ', part_1(input))

def part_2(input):
    return

print('Part 2: ', part_2(input))
