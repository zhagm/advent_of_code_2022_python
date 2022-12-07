with open("data/day07_input.txt") as f:
    input = f.read().split('\n$ ')

class Dir:
    def __init__(self, size, parent):
        self.size = size
        self.parent = parent
        self.children = {}

    def get_size(self):
        if self.size:
            return self.size
        size_sum = 0
        for key in self.children.keys():
            child = self.children.get(key)
            size_sum += child.get_size() if isinstance(child, Dir) else child
        self.size = size_sum
        return size_sum
    
    def children_within_limit(self, limit, is_upper_limit = True):
        kids = []
        for child in self.children.values():
            if not isinstance(child, int):
                if (is_upper_limit and child.size <= limit) or (not is_upper_limit and child.size >= limit):
                    kids.append(child.size)
                kids += child.children_within_limit(limit, is_upper_limit)
        return kids

def parse_dir_tree(groups):
    root = Dir(0, None)
    curr = root
    for group in groups:
        lines = group.split('\n')
        action, output = lines[0], lines[1:]
        if action.startswith('cd'):
            dir = action.split(' ')[1]
            if dir == '..':
                curr = curr.parent
            elif dir != '/':
                curr = curr.children.get(dir)
        if action.startswith('ls'):
            for [first, second] in [item.split(' ') for item in output]:
                curr.children[second] = Dir(0, curr) if first == 'dir' else int(first)
    return root

ROOT = parse_dir_tree(input)
ROOT.get_size()

def part_1(root):
    return sum(root.children_within_limit(100000))

print('Part 1: ', part_1(ROOT))

def part_2(root):
    curr_unused = 70000000 - root.size
    target_unused = 30000000
    min_size = target_unused - curr_unused

    return min(root.children_within_limit(min_size, False))

print('Part 2: ', part_2(ROOT))
