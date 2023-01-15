from functools import cmp_to_key

with open("data/day13_input.txt") as f:
    raw_input = f.read()
    part1_input = raw_input.split('\n\n')
    part2_input = list(filter(None, raw_input.split('\n')))

def get_num(s):
    close_index = 0
    while s[close_index].isnumeric():
        close_index += 1
    return int(s[:close_index]) if close_index else 0, close_index

def compare(first, second):
    if first and second:
        first = first[1:] if first[0] == ',' else first
        second = second[1:] if second[0] == ',' else second
        l, r = first[0], second[0]
    else:
        if not first and not second:
            return 0
        return 1 if second else -1
    if l == "[":
        if r == "]":
            return -1
        elif r == "[":
            return compare(first[1:], second[1:])
        else:
            _, r_end = get_num(second)
            return compare(first[1:], f"{second[:r_end]}]{second[r_end:]}")
    elif l == "]":
        if r == "]":
            return compare(first[1:], second[1:])
        return 1
    else:
        l_num, l_end = get_num(first)
        r_num, r_end = get_num(second)
        if r_end:
            if r_num == l_num:
                return compare(first[l_end:], second[r_end:])
            return r_num - l_num
        elif r == "]":
            return -1
        elif r == "[":
            return compare(f"{first[:l_end]}]{first[l_end:]}", second[1:])
    return -1


def part_1(packets):
    right_orders = []
    for index, pair in enumerate(packets):
        if compare(*pair.split('\n')) > 0:
            right_orders.append(index + 1)
    return sum(right_orders)


print('Part 1: ', part_1(part1_input))

def part_2(packets):
    d1, d2 = '[[2]]', '[[6]]'
    packets += [d1, d2]
    packets.sort(reverse=True, key=cmp_to_key(compare))
    return (packets.index(d1) + 1) * (packets.index(d2) + 1)

print('Part 2: ', part_2(part2_input))

# int, int -> first is lower or both are equal
# [], [] -> compare each value of each list, left list must be shorter or equal
# int, [] or [], int -> convert int to list


# L: "["
# right order if R is: ---
# wrong order if R is: "]"
# continue if R is: "[" or int (for int, add right bracket and continue)
# L: int
# right order if R is: > int, 
# wrong order if R is: "]" or < int
# continue if R is: "[" or == int
# L: "]"
# right order if R is: "[" or int
# wrong order if R is: ---
# continue if R is: "]"