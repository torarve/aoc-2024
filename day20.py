with open("input20.txt") as i:
    input = [x.strip() for x in i.readlines()]

test_data = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############""".split("\n")

# input = test_data

map = "".join(input)
w, h = len(input[0]), len(input)
start, end = map.index("S"), map.index("E")

def print_map():
    for r in range(h):
        print(map[r*w:(r+1)*w])

distances = [None]*w*h
working_set = [end]
current = 0
while len(working_set)>0:
    next = []
    for i in working_set:
        if distances[i] is None:
            distances[i] = current
        next = [x for x in [i-1, i-w, i+1, i+w] if map[x]!="#" and distances[x] is None]
    working_set = next
    current += 1

print(distances[start])
original = distances[start]

def get_cheats(cheat_length, limit):
    count = 0
    for i in range(0, w*h):
        if distances[i] is None: continue
        for j in range(i+1, w*h):
            if distances[j] is None: continue
            x1, y1, x2, y2 = i%w, i//w, j%w, j//w
            if abs(x1-x2) + abs(y1-y2)<=cheat_length:
                k = 0
                if distances[i] > distances[j]:
                    k = distances[start]-distances[i] + distances[j] + abs(x1-x2) + abs(y1-y2)
                elif distances[i] < distances[j]:
                    k = distances[start]-distances[j] + distances[i] + abs(x1-x2) + abs(y1-y2)
                if original-k>=limit:
                    count += 1
    return count


print(w, h)
print(get_cheats(2, 100))
print(get_cheats(20, 100))
