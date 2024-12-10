with open("input10.txt") as i:
    input = [x.strip() for x in i.readlines()]

test_data = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""".split("\n")

#input = test_data

size = len(input[0])
data = "".join(input)

start_positions = [i for i,x in enumerate(data) if x=="0"]

counts = []
for start_pos in start_positions:
    count = 0
    visited = set([start_pos])
    while len(visited)>0:
        tmp = set()
        for pos in visited:
            height = int(data[pos])
            if pos%size > 0 and int(data[pos-1])==height+1:
                tmp.add(pos-1)
            if pos%size < size-1 and int(data[pos+1])==height+1:
                tmp.add(pos+1)
            if pos//size > 0 and int(data[pos-size])==height+1:
                tmp.add(pos-size)
            if pos//size < size-1 and int(data[pos+size])==height+1:
                tmp.add(pos+size)
        count += len([x for x in tmp if data[x]=="9"])
        visited = tmp

    counts.append(count)

print(sum(counts))

cache: dict[int, int] = {}
def calculate_score(pos):
    if data[pos]=="9":
        cache[pos] = 1
        return 1
    if pos in cache.keys():
        return cache[pos]
    
    height = int(data[pos])
    score = 0
    if pos%size > 0 and int(data[pos-1])==height+1:
        score += calculate_score(pos-1)
    if pos%size < size-1 and int(data[pos+1])==height+1:
        score += calculate_score(pos+1)
    if pos//size > 0 and int(data[pos-size])==height+1:
        score += calculate_score(pos-size)
    if pos//size < size-1 and int(data[pos+size])==height+1:
        score += calculate_score(pos+size)
    cache[pos] = score

    return score

scores = []
for start_pos in start_positions:
    scores.append(calculate_score(start_pos))

print(sum(scores))