import itertools


with open("input08.txt") as i:
    input = [x.strip() for x in i.readlines()]

test_data = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............""".split("\n")

# input = test_data

data = "".join(input)
size = len(input[0])

antennas = {}
for i, x in enumerate(data):
    if x == ".": continue

    tmp = antennas.get(x, [])
    tmp.append(i)
    antennas[x] = tmp

antinodes = []
for freq in antennas.keys():
    for p1, p2 in itertools.combinations(antennas[freq], 2):
        x1, y1 = p1%size, p1//size
        x2, y2 = p2%size, p2//size
        dx, dy = x2-x1, y2-y1

        antinodes.append((x1-dx, y1-dy))
        antinodes.append((x2+dx, y2+dy))
    
antinodes = [(x,y) for x,y in antinodes if x>=0 and x<size and y>=0 and y<size]
print(len(set(antinodes)))

antinodes = []
for freq in antennas.keys():
    for p1, p2 in itertools.combinations(antennas[freq], 2):
        x1, y1 = p1%size, p1//size
        x2, y2 = p2%size, p2//size
        dx, dy = x2-x1, y2-y1

        antinodes.append((x1,y1))
        antinodes.append((x2,y2))
        for i in range(size):
            antinodes.append((x1-dx*i, y1-dy*i))
            antinodes.append((x2+dx*i, y2+dy*i))

antinodes = [(x,y) for x,y in antinodes if x>=0 and x<size and y>=0 and y<size]
print(len(set(antinodes)))
