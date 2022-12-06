with open("data/day06_input.txt") as f:
    input = f.read()

def day_6(input, substr_len):
    curr = ''
    for i in range(len(input)):
        item = input[i]
        if len(curr) == substr_len:
            curr = curr[1:]
        curr += item
        if len(set(curr)) == substr_len:
            return i + 1

print('Part 1: ', day_6(input, 4))
print('Part 2: ', day_6(input, 13))
