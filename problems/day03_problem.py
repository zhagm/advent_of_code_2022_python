import string

with open("data/day03_input.txt") as f:
    input = f.read().splitlines()

PRIORITY_INDEX_STRING = '#' + string.ascii_lowercase + string.ascii_uppercase

def find_common_char(strs):
    for char in strs[0]:
        if all(map(lambda s: char in s, strs[1:])):
            return char
    return -1

#########################

def part_1(input):
    priority_sum = 0
    for r in input:
        half_len = len(r)//2
        first, second = r[:half_len], r[half_len:]
        duplicate = find_common_char([first, second])
        priority_sum += PRIORITY_INDEX_STRING.find(duplicate)
    return priority_sum

print('Part 1: ', part_1(input))

def part_2(input):
    priority_sum = 0
    for i in range(0, len(input), 3):
        duplicate = find_common_char(input[i:i+3])
        priority_sum += PRIORITY_INDEX_STRING.find(duplicate)
    return priority_sum

print('Part 2: ', part_2(input))
