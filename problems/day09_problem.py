with open("data/day09_input.txt") as f:
    input = f.read().splitlines()
    input = [row.split(' ') for row in input]
    input = [[move[0], int(move[1])] for move in input]


class Point:
    def __init__(self, name, x, y, track_visited = False):
        self.name = name
        self.x = x
        self.y = y
        self.visited = {F"{x},{y}"} if track_visited else None


    def move(self, dir):
        if dir == 'U':
            self.y += 1
        elif dir == 'R':
            self.x += 1
        elif dir == 'D':
            self.y -= 1
        elif dir == 'L':
            self.x -= 1


    def follow(self, other):
        x_diff = self.x - other.x
        x_diff_abs = abs(x_diff)
        y_diff = self.y - other.y
        y_diff_abs = abs(y_diff)

        # If they are touching, skip moving
        if x_diff_abs <= 1 and y_diff_abs <= 1:
            return
        
        x_move = 'R' if x_diff < 0 else 'L'
        y_move = 'U' if y_diff < 0 else 'D'
        if x_diff_abs >= 1 and y_diff_abs >= 1:
            self.move(x_move)
            self.move(y_move)
        elif x_diff_abs > 1:
            self.move(x_move)
        elif y_diff_abs > 1:
            self.move(y_move)
        if self.visited:
            self.visited.add(F"{self.x},{self.y}")


    def print(self, others):
        max_x = max(self.x, *[o.x for o in others])
        max_y = max(self.y,  *[o.y for o in others])
        min_x = min(self.x, *[o.x for o in others])
        min_y = min(self.y,  *[o.y for o in others])
        grid_x = range(min_x, max_x + 1)
        grid_y = range(min_y, max_y + 1)[::-1]

        grid = []
        for y in grid_y:
            row = []
            for x in grid_x:
                printed = False
                for pt in [self, *others]:
                    if pt.x == x and pt.y == y:
                        row.append(pt.name)
                        printed = True
                        break
                if not printed:
                    row.append('.')
            grid.append(row)
        print('\n'.join([''.join(row) for row in grid]), '\n')


def day_9(moves, knots_count):
    H = Point('H', 0, 0)
    others = [Point(str(i), 0, 0, True if i == knots_count else False) for i in range(1, knots_count + 1)]
    for [dir, steps] in moves:
        for i in range(steps):
            H.move(dir)
            prev = H
            for point in others:
                point.follow(prev)
                prev = point
    return len(others[-1].visited)

print('Part 1: ', day_9(input, 1))
print('Part 2: ', day_9(input, 9))
