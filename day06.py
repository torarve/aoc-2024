with open("input06.txt") as i:
    input = [x.strip() for x in i.readlines()]

test_data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".split("\n")

# input = test_data

class Map:

    def __init__(self, rows: list[str]):
        self.rows = list("".join(rows))
        self.size = len(rows[0])
        self.position = self.find_start()
        self.direction = (0,-1)
        self.states = set()

    def find_start(self):
        i = self.rows.index("^")
        return (i%self.size, i//self.size)
    
    def at(self, x, y):
        return self.rows[x + y*self.size]
    
    def step(self) -> bool:
        x, y = self.position
        self.rows[x+y*self.size] = "X"
        x, y = self.position[0]+self.direction[0], self.position[1]+self.direction[1]
        if x<0 or y<0 or x>=self.size or y>=self.size:
            return False
        
        if self.at(x,y)=="#":
            turns = {
                (0, -1): (1, 0),
                (1, 0): (0, 1),
                (0, 1): (-1, 0),
                (-1, 0): (0, -1)
            }
            self.direction = turns[self.direction]
            return self.step() 

        self.rows[x+y*self.size] = 'o'
        self.position = x, y
        return True
    
    def step2(self) -> bool:
        while True:
            x, y = self.position[0], self.position[1]
            dx, dy = self.direction

            state = (x, y, dx, dy)
            if state in self.states:
                return True
            
            self.states.add(state)

            if not self.step():
                return False

    
map = Map(input)

steps = 0
while map.step():
    steps += 1

print(len([x for x in map.rows if x == "X"]))

indexes = [i for i in range(len(map.rows)) if map.rows[i] == "X"]

count = 0
for i in indexes:
    x = i%map.size
    y = i//map.size
    map = Map(input)
    map.rows[x+y*map.size] = "#"
    if map.step2():
        count += 1

print(count)