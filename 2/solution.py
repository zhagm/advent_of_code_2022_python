with open("input.txt") as f:
    input = f.read().splitlines()


with open("test_input.txt") as f:
    test_input = f.read().splitlines()

# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# Your total score is the sum of your scores for each round.
# The score for a single round is the score for the shape you selected
# (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round
# (0 if you lost, 3 if the round was a draw, and 6 if you won)

# rock > scissors
# scissors > paper
# paper > rock

def part_1(rounds):
    score = 0
    points_map = { 'X': 1, 'Y': 2, 'Z': 3 }
    score_map = { 'A X': 3, 'A Y': 6, 'B Y': 3, 'B Z': 6, 'C Z': 3, 'C X': 6 }
    for round in rounds:
        score = score + points_map[round[-1]] + (score_map[round] if round in score_map else 0)
    return score

print('Part 1: ', part_1(input))

# X means you need to lose
# Y means you need to draw
# Z means you need to win

# A > C
# C > B
# B > A

def get_move(opp, outcome):
    if (outcome == 'Y'):
        return opp
    if (outcome == 'Z'):
        if (opp == 'A'):
            return 'B'
        if (opp == 'B'):
            return 'C'
        if (opp == 'C'):
            return 'A'
    if (outcome == 'X'):
        if (opp == 'A'):
            return 'C'
        if (opp == 'B'):
            return 'A'
        if (opp == 'C'):
            return 'B'

def part_2(rounds):
    score = 0
    points_map = { 'X': 0, 'Y': 3, 'Z': 6, 'A': 1, 'B': 2, 'C': 3 }
    for round in rounds:
        [opp, outcome] = round.split(' ')
        score = score + points_map[outcome] + points_map[get_move(opp, outcome)]
    return score

print('Part 2: ', part_2(input))
