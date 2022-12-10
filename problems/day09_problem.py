with open("data/day09_input.txt") as f:
    input = f.read().splitlines()
    input = [row.split(' ') for row in input]
    input = [[move[0], int(move[1])] for move in input]


class Point:
    def __init__(self, name, x, y, track_visited = False):
        self.name = name
        self.x = x
        self.y = y
        self.visited = { F"{x},{y}": True } if track_visited else None
    
    def move(self, dir):
        if dir == 'U':
            self.y += 1
        elif dir == 'R':
            self.x += 1
        elif dir == 'D':
            self.y -= 1
        elif dir == 'L':
            self.x -= 1
        if self.visited:
            self.visited[F"{self.x},{self.y}"] = True

    def follow(self, other):
        x_diff = self.x - other.x
        x_diff_abs = abs(x_diff)
        y_diff = self.y - other.y
        y_diff_abs = abs(y_diff)

        # If they are touching, skip moving
        if x_diff_abs <= 1 and y_diff_abs <= 1:
            return

        if x_diff_abs >= 1 and y_diff_abs >= 1:
            self.x += 1 if x_diff < 0 else -1
            self.y += 1 if y_diff < 0 else -1
        elif x_diff_abs > 1:
            self.x += 1 if x_diff < 0 else -1
        elif y_diff_abs > 1:
            self.y += 1 if y_diff < 0 else -1
        if self.visited:
            self.visited[F"{self.x},{self.y}"] = True
        
    
    def print(self, others):
        max_x = max(self.x, *[o.x for o in others]) + 1
        max_y = max(self.y,  *[o.y for o in others]) + 1
        min_x = min(self.x, *[o.x for o in others])
        min_y = min(self.y,  *[o.y for o in others])
        grid_x = range(min_x, max_x)
        grid_y = range(min_y, max_y)[::-1]

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


def part_1(input):
    H = Point('H', 0, 0)
    T = Point('T', 0, 0, True)
    for [dir, steps] in input:
        for i in range(steps):
            H.move(dir)
            T.follow(H)
    return len(T.visited.values())


print('Part 1: ', part_1(input))

def part_2(input):
    H = Point('H', 0, 0)
    others = [Point(str(i + 1), 0, 0, True if i == 8 else False) for i in range(9)]
    for [dir, steps] in input:
        for i in range(steps):
            H.move(dir)
            prev = H
            for point in others:
                point.follow(prev)
                prev = point
    return len(others[-1].visited)

print('Part 2: ', part_2(input))
