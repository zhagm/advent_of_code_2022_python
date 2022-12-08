with open("data/day08_input.txt") as f:
    input = f.read().splitlines()

def parse_input(input):
    rows = [[int(t) for t in line] for line in input]
    cols = [[rows[x][i] for x in range(len(rows))] for i in range(len(rows))]
    return rows, cols

ROWS, COLS = parse_input(input)

def part_1(rows, cols):
    visible_trees = []
    row_index = 1
    for row in rows[1:-1]:
        col_index = 1
        for tree in row[1:-1]:
            if (tree > max(row[:col_index])) or \
                (tree > max(row[col_index + 1:])) or \
                (tree > max(cols[col_index][:row_index])) or \
                (tree > max(cols[col_index][row_index + 1:])):
                visible_trees.append(tree)
            col_index += 1
        row_index += 1
    perimeter = (2 * (len(rows) + len(rows[0])) - 4)
    return len(visible_trees) + perimeter

print('Part 1: ', part_1(ROWS, COLS))

def get_scenic_score(tree, trees_list):
    score = 1
    view_scores = []
    for trees in trees_list:
        trees_score = 0
        try:
            trees_score = next(i for i,t in enumerate(trees) if t >= tree) + 1
        except:
            trees_score = len(trees)
        view_scores.append(trees_score)
        score *= trees_score
    return score

def part_2(rows, cols):
    max_score = 0
    row_index = 1
    for row in rows[1:-1]:
        col_index = 1
        for tree in row[1:-1]:
            score = get_scenic_score(tree, [row[:col_index][::-1], row[col_index + 1:], cols[col_index][:row_index][::-1], cols[col_index][row_index + 1:]])
            if score > max_score:
                max_score = score
            col_index += 1
        row_index += 1
    return max_score

print('Part 2: ', part_2(ROWS, COLS))