import re


with open("input14.txt") as i:
    input = [x.strip() for x in i.readlines()]

test_data = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3""".split("\n")

w, h = 101, 103

# w, h = 11, 7
# input = test_data

start_robots = []
for l in input:
    a, b, c, d = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", l).groups()
    start_robots.append((int(a),int(b),int(c),int(d)))

robots = start_robots
for i in range(100):
    tmp = []
    for x, y, dx, dy in robots:
        tmp.append(((x+dx) % w, (y+dy)%h, dx, dy))
    robots = tmp

q1 = [(x,y,dx,dy) for x,y,dx,dy in robots if x<w//2 and y<h//2]
q2 = [(x,y,dx,dy) for x,y,dx,dy in robots if x<w//2 and y>h//2]
q3 = [(x,y,dx,dy) for x,y,dx,dy in robots if x>w//2 and y<h//2]
q4 = [(x,y,dx,dy) for x,y,dx,dy in robots if x>w//2 and y>h//2]

print(len(q1)*len(q2)*len(q3)*len(q4))

robots = start_robots
for i in range(w*h):
    robots = [((x+dx)%w, (y+dy)%h, dx, dy) for x, y, dx, dy in robots]
    positions = [(x,y) for x,y, _, __ in robots]
    map = ["."]*(w*h)
    for x, y in positions:
        map[x+y*w] = "*"
    map_str = "".join(map)
    if map_str.find("*******************************")>0:
        for r in range(h):
            print(map_str[r*w:(r+1)*w])

        print(i+1)
        break

