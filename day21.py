import functools


with open("input21.txt") as i:
    input = [x.strip() for x in i.readlines()]

test_data = """029A
980A
179A
456A
379A""".split("\n")

# input = test_data

# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+
numeric_keys = {
    "7": (0, 0), "8": (1, 0), "9": (2, 0),
    "4": (0, 1), "5": (1, 1), "6": (2, 1),
    "1": (0, 2), "2": (1, 2), "3": (2, 2),
                 "0": (1, 3), "A": (2, 3),
}

#    +---+---+
#    | ^ | A |
#+---+---+---+
#| < | v | > |
#+---+---+---+
directional_keys = {
                 "^": (1, 0), "A": (2, 0),
    "<": (0, 1), "v": (1, 1), ">": (2,1)
}

allowed_num_pos = [v for v in numeric_keys.values()]
allowed_dir_pos = [v for v in directional_keys.values()]
pos = (2,3)
x, y = pos


def find_keystrokes(src, target, directional):
    if src == target: return ["A"]
    if not directional and not src in allowed_num_pos: return []
    if directional and not src in allowed_dir_pos: return []
    x1, y1 = src
    x2, y2 = target
    res = []
    if x1<x2: res.extend([">"+s for s in find_keystrokes((x1+1, y1), target, directional)])
    elif x1>x2: res.extend(["<"+s for s in find_keystrokes((x1-1, y1), target, directional)])
    if y1<y2: res.extend(["v"+s for s in find_keystrokes((x1, y1+1), target, directional)])
    elif y1>y2: res.extend(["^"+s for s in find_keystrokes((x1, y1-1), target, directional)])
    return res


@functools.cache
def find_shortest_to_click(a, b, depth=2):
    # Assume we start at A always?
    opts = find_keystrokes(directional_keys[a], directional_keys[b], True)
    if depth == 1:
        return min([len(x) for x in opts])
    
    tmps = []
    for o in opts:
        tmp = []
        tmp.append(find_shortest_to_click("A", o[0], depth-1))
        for i in range(1, len(o)):
            tmp.append(find_shortest_to_click(o[i-1], o[i], depth-1))
        tmps.append(sum(tmp))

    return min(tmps)


def find_shortest(code, levels):
    pos = numeric_keys["A"]
    shortest = 0
    for key in code:
        possible_key_sequences = find_keystrokes(pos, numeric_keys[key], False)
        tmps = []
        for sequence in possible_key_sequences:
            tmp = []
            tmp.append(find_shortest_to_click("A", sequence[0], levels))
            for i in range(1, len(sequence)):
                tmp.append(find_shortest_to_click(sequence[i-1], sequence[i], levels))

            tmps.append(sum(tmp))
        pos = numeric_keys[key]
        shortest += min(tmps)
    return shortest


def find_total_complexity(codes, levels):
    complexities = []
    for code in input:
        s = find_shortest(code, levels)
        complexities.append(s*int(code[:-1]))
    return sum(complexities)


print(find_total_complexity(input, 2))
print(find_total_complexity(input, 25))

