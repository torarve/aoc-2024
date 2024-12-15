with open("input15.txt") as i:
    input = [x.strip() for x in i.readlines()]

test_data = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^""".split("\n")

# input = test_data

map = []
w = len(input[0])
h = 0

while input[h]!="":
    map.extend([x for x in input[h]])
    h+=1

def print_map():
    for y in range(h):
        print("".join(map[y*w:(y+1)*w]))

steps = "".join(input[h+1:])

pos = map.index("@")
x, y = pos%w, pos//w

step_direction = {
    "<": (-1, 0),
    "^": (0,-1),
    ">": (1, 0),
    "v": (0, 1)
}

for dx, dy in [step_direction[x] for x in steps]:
    pos = (x+dx) + (y+dy)*w
    if map[pos]==".":
        map[x+y*w] = "."
        x, y = x+dx, y+dy
    elif map[pos] != "#":
        xx, yy = x+dx, y+dy
        while map[xx+yy*w] == 'O':
            xx, yy = xx+dx, yy+dy
        if map[xx+yy*w]==".":
            map[x+y*w] = "."
            x, y = x+dx, y+dy
            map[xx+yy*w] ="O"
        
    map[x+y*w] = "@"

# print_map()
# print()

scores = [i%w + i//w * 100 for (i, b) in enumerate(map) if b=="O"]
print(sum(scores))

map = []
w = len(input[0])*2
h = 0

while input[h]!="":
    l = input[h].replace("#", "##").replace(".", "..").replace("O", "[]").replace("@", "@.")
    map.extend([x for x in l])
    h+=1

pos = map.index("@")
x, y = pos%w, pos//w

# print_map()

def can_push(x, y, dy):
    above = map[x+(y+dy)*w:(x+1)+(y+dy)*w+1 ]
    if "#" in above:
        return False
    elif "[" in above or "]" in above:
        boxes = []
        if above[0] == "]":
            boxes.append((x-1, y+dy))
        elif above[0] == "[":
            boxes.append((x, y+dy))
        if above[1] == "[":
            boxes.append((x+1, y+dy))
        
        return all([can_push(*args, dy) for args in boxes])
    
    return True

def push(x, y, dy):
    above = map[x+(y+dy)*w:(x+1)+(y+dy)*w+1]
    if "[" in above or "]" in above:
        if above[0] == "]":
            push(x-1, y+dy, dy)
        elif above[0] == "[":
            push(x, y+dy, dy)
        if above[1] == "[":
            push(x+1, y+dy, dy)

    map[x+(y+dy)*w] = map[x+y*w]
    map[(x+1)+(y+dy)*w] = map[(x+1)+y*w]
    map[x+y*w] = "."
    map[(x+1)+y*w] = "."

for dx, dy in [step_direction[x] for x in steps]:
    pos = (x+dx) + (y+dy)*w
    if map[pos]==".":
        map[x+y*w] = "."
        x, y = x+dx, y+dy
    elif map[pos] != "#":
        xx, yy = x+dx, y+dy
        if dy == 0:
            while map[xx+y*w] == ']' or map[xx+y*w] == '[':
                xx = xx+dx*2
            if map[xx+y*w]==".":
                map[x+y*w] = "."
                for i in range(xx, x, -dx):
                    map[i+y*w] = map[(i-dx)+y*w]
                x, y = x+dx, y+dy
                map[x+y*w] = "@"
        else:
            xx, yy = x, y+dy
            if map[x+(y+dy)*w] == "]":
                xx -= 1
            
            if can_push(xx, yy, dy):
                push(xx, yy, dy)
                map[x+y*w] = "."
                x, y = x+dx, y+dy
        
    map[x+y*w] = "@"

# print_map()

scores = [i%w + i//w * 100 for (i, b) in enumerate(map) if b=="["]
print(sum(scores))
