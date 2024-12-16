with open("input16.txt") as i:
    input = [x.strip() for x in i.readlines()]

test_data = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############""".split("\n")

# input = test_data

map = "".join(input)
w = len(input[0])
start = map.find("S")
end = map.find("E")
current = [(start, 1, 0, 0, set())]
found: dict[int,int,int,int,int] = {}
part_of_best_paths = set()
current_best = None
visited_on_the_way = {}
while len(current)>0:
    next_to_visit = []
    for pos, dx, dy, score, path in current:
        if current_best is not None and score>current_best:
            continue
        x, y = pos%w, pos//w
        key = (x, y, dx, dy)
        if key in found.keys() and found.get(key,0)<score:
            continue
        found[key] = score

        new_path = path.union([pos])
        
        if pos == end:
            if current_best is None or score<current_best:
                current_best = score
                part_of_best_paths = set(new_path)
            elif score == current_best:
                part_of_best_paths.update(new_path)
        
        adjacent = [pos-1, pos-w, pos+1, pos+w]
        adjacent = [p for p in adjacent if map[p]!='#']
        
        for next_pos in adjacent:
            if next_pos == (x+dx)+(y+dy)*w:
                # Move ahead
                next_to_visit.append(((x+dx)+(y+dy)*w, dx, dy, score+1, new_path))
            else:
                # Turn!!
                if (x+dy)+(y-dx)*w == next_pos:
                    # turn left
                    next_to_visit.append(((x+dy)+(y-dx)*w, dy, -dx, score+1001, new_path))
                elif (x-dy)+(y+dx)*w == next_pos:
                    # turn right
                    next_to_visit.append(((x-dy)+(y+dx)*w, -dy, dx, score+1001, new_path))
                else:
                    next_to_visit.append(((x+dx)+(y-dy)*w, -dx, -dy, score+2001, new_path))

    seen = {}
    for (pos, dx, dy, score, path) in next_to_visit:
        k = (pos, dx, dy, score)
        p = seen.get(k, set())
        seen[k] = p.union(path)

    current = []
    for (pos, dx, dy, score), path in seen.items():
        current.append((pos, dx, dy, score, path))

print(current_best)

print(len(set(part_of_best_paths)))