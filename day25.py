with open("input25.txt") as f:
    input = [x.strip() for x in f.readlines()]

test_data = """#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####""".split("\n")

#input = test_data

locks = []
keys = []

def read_schematic(schematic):
    h = len(schematic)//w
    t = [schematic[j:h*w:w].count("#")-1 for j in range(w)]
    if all(x=="." for x in schematic[0:w]):
        keys.append(t)
    else:
        locks.append(t)

tmp = ""
w = len(input[0])
for i in input:
    if i == "":
        read_schematic(tmp)
        tmp = ""
    else:
        tmp += i
read_schematic(tmp)

part1 = 0
for key in keys:
    for lock in locks:
        if all([x+y<6 for x,y in zip(key, lock)]):
            part1 += 1

print(part1)