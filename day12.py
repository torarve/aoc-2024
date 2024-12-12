with open("input12.txt") as i:
    input = [x.strip() for x in i.readlines()]
    # input = i.read().strip()

test_data = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE""".split("\n")# # 

# input = test_data


data = "".join(input)
size = len(input[0])


def adjacent(pos:int):
    x, y = pos%size, pos//size
    if x>0:
        yield pos-1
    if x<size-1:
        yield pos+1
    if y>0:
        yield pos-size
    if y<size-1:
        yield pos+size


visited = set()
areas = []
for i in range(size*size):
    if i in visited: continue
    
    calculated_area = 0
    calculated_permiter = 0
    next = [i]
    left1, top1, right1, bottom1 = [None]*size, [None]*size, [None]*size, [None]*size
    left, top, right, bottom = [None]*size*size, [None]*size*size, [None]*size*size, [None]*size*size
    while len(next)>0:
        p = next.pop()
        if p in visited: continue
        visited.add(p)
        calculated_area += 1
        neighbours = [x for x in adjacent(p) if data[x]==data[p]] 
        x, y = p%size, p//size
        if x==0 or data[p-1] != data[p]:
            left1[y] = x
            left[x+y*size] = True
        if x==size-1 or data[p+1] != data[p]:
            right1[y] = x
            right[p] = True
        if y==0 or data[p-size] != data[p]:
            top1[x] = y
            top[x+y*size] = True
        if y==size-1 or data[p+size] != data[p]:
            bottom1[x] = y
            bottom[x+y*size] = True
        
        calculated_permiter += 4 - len(neighbours)
        next.extend([x for x in neighbours if x not in visited])

    def count_changes(values: list[int]) -> int:
        count = 0
        for i in range(1,len(values)):
            if values[i]!=values[i-1]:
                count += 1

        return count

    top_count = 0
    for i in range(size):
        row = top[i*size:(i+1)*size]
        if any(row):
            if row[0] is not None: top_count += 1
            for j in range(1,size):
                if row[j] is not None and row[j-1] != row[j]: top_count += 1

    bottom_count = 0
    for i in range(size):
        row = bottom[i*size:(i+1)*size]
        if any(row):
            if row[0] is not None: bottom_count += 1
            for j in range(1,size):
                if row[j] is not None and row[j-1] != row[j]: bottom_count += 1

    left_count = 0
    for i in range(size):
        col = left[i:size*size:size]
        if any(col):
            if col[0] is not None: left_count += 1
            for j in range(1,size):
                if col[j] is not None and col[j-1] != col[j]: left_count += 1
        
    right_count = 0
    for i in range(size):
        col = right[i:size*size:size]
        if any(col):
            if col[0]: right_count += 1
            for j in range(1,size):
                if col[j] is not None and col[j-1] != col[j]: right_count += 1

    areas.append((calculated_permiter, calculated_area, left_count+top_count+right_count+bottom_count))


print(sum([a*b for a,b,_ in areas]))
print(sum([a*b for _,a,b in areas]))