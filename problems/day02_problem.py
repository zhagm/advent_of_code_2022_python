with open("data/day02_input.txt") as f:
    input = f.read().splitlines()

def part_1(rounds):
    score = 0
    points_map = { 'X': 1, 'Y': 2, 'Z': 3 }
    score_map = { 'A X': 3, 'A Y': 6, 'B Y': 3, 'B Z': 6, 'C Z': 3, 'C X': 6 }
    for round in rounds:
        score = score + points_map[round[-1]] + (score_map[round] if round in score_map else 0)
    return score

print('Part 1: ', part_1(input))

def part_2(rounds):
    score = 0
    points_map = { 'X': 0, 'Y': 3, 'Z': 6, 'A X': 3, 'A Y': 1, 'A Z': 2, 'B X': 1, 'B Y': 2, 'B Z': 3, 'C X': 2, 'C Y': 3, 'C Z': 1 }
    for round in rounds:
        score = score + points_map[round[-1]] + points_map[round]
    return score

print('Part 2: ', part_2(input))
