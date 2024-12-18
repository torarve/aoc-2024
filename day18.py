with open("input18.txt") as i:
    input = [x.strip() for x in i.readlines()]

test_data = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0""".split("\n")

def parse(l: str) -> tuple[int, int]:
    x, y = l.split(",")
    return int(x), int(y)

w, h = 71, 71
steps_part1 = 1024

# w, h = 7, 7
# input = test_data
# steps_part1 = 12

corrupt_positions = [parse(x) for x in input]

map =["."] * (w*h)

def print_map():
    for r in range(h):
        print("".join(map[r*w:(r+1)*w]))

def get(x, y):
    if 0<=x and x<w and 0<=y and y<h:
        return map[x+y*w]
    return None

for i in range(steps_part1):
    x, y = corrupt_positions[i]
    map[x+y*w] = "#"

print_map()

def simulate():
    visited = set()
    current = [(0,0)]
    steps = 0
    while (w-1, h-1) not in current and len(current)>0:
        next_set = []
        for x,y in current:
            neighbours = [(-1,0), (0,-1), (1,0), (0,1)]
            for dx, dy in neighbours:
                xx, yy = x+dx, y+dy
                if 0<=xx and xx<w and 0<=yy and yy<h and get(xx,yy)!="#" and (xx,yy) not in visited:
                    next_set.append((xx,yy))
                    visited.add((xx,yy))
        steps += 1
        current = next_set
    
    if len(current)==0:
        return None
    
    return steps

print(simulate())

steps = steps_part1 - 1
while simulate() is not None:
    steps += 1
    x, y = corrupt_positions[steps]
    map[x+y*w] = "#"

print(corrupt_positions[steps])
