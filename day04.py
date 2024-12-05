with open("input04.txt") as i:
    input = [x.strip() for x in i.readlines()]

test_data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".split("\n")

#input = test_data

class Grid:

    def __init__(self, size: int, values: str):
        self.size = size
        self.values = values

    def words_at(self, x, y, word="XMAS"):
        word_size = len(word)
        found_count = 0
        current_pos = x+y*self.size
        reverse_word = word[::-1]

        # Left to right
        if word_size+x <= self.size:
            tmp = self.values[current_pos:current_pos+word_size]
            if tmp == word:
                found_count += 1
            if tmp == reverse_word:
                found_count += 1
        
        # Top to bottom
        if word_size+y <= self.size:
            tmp = self.values[current_pos:x+(y+word_size)*self.size:self.size]
            if tmp == word:
                found_count += 1
            if tmp == reverse_word:
                found_count += 1

        # Diagonals
        if word_size+x <= self.size and word_size+y <= self.size:
            tmp = self.values[current_pos:word_size+current_pos+self.size*word_size:self.size+1]
            if tmp == word:
                found_count += 1
            if tmp == reverse_word:
                found_count += 1

        if x>=word_size-1 and y+word_size <= self.size:
            tmp = self.values[current_pos:-word_size+current_pos+self.size*word_size:self.size-1]
            if tmp == word:
                found_count += 1
            if tmp == reverse_word:
                found_count += 1
        
        return found_count
    
    def at(self, x, y):
        return self.values[x + y*self.size]

    def is_xmas(self, x, y):
        if x == 0 or y == 0 or x == self.size-1 or y == self.size-1:
            return False
        
        if self.at(x,y) != "A":
            return False
        
        if self.at(x-1,y-1) == "X" or self.at(x+1,y-1)=="X" or self.at(x-1,y+1)=="X" or self.at(x+1,y+1)=="X":
            return False

        if self.at(x-1,y-1) == "A" or self.at(x+1,y-1)=="A" or self.at(x-1,y+1)=="A" or self.at(x+1,y+1)=="A":
            return False
        
        if self.at(x-1,y-1)=="M" and self.at(x+1, y+1) != "S":
            return False
        
        if self.at(x-1,y-1)=="S" and self.at(x+1,y+1) != "M":
            return False

        if self.at(x+1,y-1)=="M" and self.at(x-1, y+1) != "S":
            return False
        
        if self.at(x+1,y-1)=="S" and self.at(x-1,y+1) != "M":
            return False
                
        return True

grid = Grid(len(input[0]), "".join(input))

count = 0
for y in range(0, grid.size):
    for x in range(0, grid.size):
        count += grid.words_at(x,y)

print(count)

count = 0
for y in range(0, grid.size):
    for x in range(0, grid.size):
        if grid.is_xmas(x,y):
            count += 1

print(count)
