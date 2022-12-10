with open("data/day09_input.txt") as f:
    input = f.read().splitlines()
    input = [row.split(' ') for row in input]
    input = [[move[0], int(move[1])] for move in input]
    print(input)


class Point:
    def __init__(self, name, x, y, track_visited = False):
        self.name = name
        self.x = x
        self.y = y
        self.visited = { F"{x},{y}": True } if track_visited else None

    def is_touching(self, other):
        if abs(self.x - other.x) <= 1 and abs(self.y - other.y) <= 1:
            return True
        return False
    
    def move(self, dir):
        if dir == 'U':
            self.y += 1
        elif dir == 'R':
            self.x += 1
        elif dir == 'D':
            self.y -= 1
        elif dir == 'L':
            self.x -= 1
        else:
            print('ERROR in move', dir)
        if self.visited:
            self.visited[F"{self.x},{self.y}"] = True

    def follow(self, other):
        x_diff = abs(self.x - other.x)
        y_diff = abs(self.y - other.y)
        print('x diff', x_diff)
        print('y diff', y_diff)
        if x_diff >= 1 and y_diff >= 1:
            if self.x - other.x < 0:
                self.x += 1
            else:
                self.x -= 1
            if self.y - other.y < 0:
                self.y += 1
            else:
                self.y -= 1
        elif x_diff > 1:
            if self.x - other.x < 0:
                self.x += 1
            else:
                self.x -= 1
        elif y_diff > 1:
            if self.y - other.y < 0:
                self.y += 1
            else:
                self.y -= 1
        if self.visited:
            self.visited[F"{self.x},{self.y}"] = True
        
    
    def print(self, other):
        max_x = max(self.x, other.x) + 1
        max_y = max(self.y, other.y) + 1

        grid = []
        for y in range(max_y)[::-1]:
            row = []
            for x in range(max_x):
                if self.x == x and self.y == y:
                    row.append(self.name)
                elif other.x == x and other.y == y:
                    row.append(other.name)
                else:
                    row.append('.')
            grid.append(row)
        print('\n'.join([''.join(row) for row in grid]), '\n')


def part_1(input):
    H = Point('H', 0, 0)
    T = Point('T', 0, 0, True)
    for [dir, steps] in input:
        print('----------- NEW MOVE')
        for i in range(steps):
            H.move(dir)
            print('-HEAD MOVE-')
            T.print(H)
            if not T.is_touching(H):
                T.follow(H)
            print('-TAIL MOVE-')
            T.print(H)
    return len(T.visited.values())


print('Part 1: ', part_1(input))

def part_2(input):
    return

print('Part 2: ', part_2(input))
