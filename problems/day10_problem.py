with open("data/day10_input.txt") as f:
    input = f.read().splitlines()

def is_20_or_40_mult(x, steps):
    diff = (x + 20) % 40
    if diff == 0:
        return x
    if diff < steps:
        return x + diff - steps

def part_1(input):
    signal_strength = 0
    cycle = 1
    x = [1]
    for line in input:
        [steps, addend] = [1, 0] if line.startswith('noop') else [2, int(line.split(' ')[1])]
        x.append(addend)
        cycle += steps
        strength_cycle = is_20_or_40_mult(cycle, steps)
        if strength_cycle:
            x_sum = sum(x) if strength_cycle == cycle else sum(x) - addend
            signal_strength += (strength_cycle * x_sum)
    return signal_strength

def get_pixel(index, x):
    mod = index % 40
    return ('' if mod else '\n') + ('█' if mod >= x - 1 and mod <= x + 1 else ' ')

def part_2(input):
    x, output = 1, []
    for line in input:
        steps, addend = 1, 0
        if line.startswith('addx'):
            steps += 1
            addend = int(line.split(' ')[1])
        for i in range(steps):
            output.append(get_pixel(len(output), x))
        x += addend
    return ''.join(output)

print('Part 1: ', part_1(input))
print('Part 2: ', part_2(input))
