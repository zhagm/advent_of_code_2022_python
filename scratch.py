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


def rock_paper_scissors(opp, you):
    if opp == you:
        return 3
    if opp == 1 and you == 2:
        return 6
    if opp == 2 and you == 3:
        return 6
    if opp == 3 and you == 1:
        return 6
    return 0


def part_1(rounds):
    score = 0
    points_map = { 'X': 1, 'Y': 2, 'Z': 3, 'A': 1, 'B': 2, 'C': 3 }
    for round in rounds:
        [opp_play, your_play] = [points_map[r] for r in round.split(' ')]
        score = score + your_play + rock_paper_scissors(opp_play, your_play)
    return score

print('Part 1: ', part_1(input))

def part_2(input):
    return

print('Part 2: ', part_2(input))