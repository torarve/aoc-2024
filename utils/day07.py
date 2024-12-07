with open("input07.txt") as i:
    input = [x.strip() for x in i.readlines()]

test_data = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""".split("\n")

# input = test_data

equations = []
for line in input:
    result, rest = line.split(": ")
    values = [int(i) for i in rest.split(" ")]
    equations.append((int(result), values))

def is_ok(expected: int, values:list[int], part2: bool = False) -> bool:
    current = set()
    current.add(values[0])
    concat = set()
    rest = values[1:]
    while len(rest)>0:
        tmp = set([x + rest[0] for x in current])
        for x in current:
            tmp.add(x * rest[0])
        if part2:
            for x in current:
                tmp.add(int(f"{x}{rest[0]}"))

        current = set(x for x in tmp if x<=expected)
        rest = rest[1:]

    return expected in current

score = 0
for e, v in equations:
    if is_ok(e, v):
        score += e

print(score)

score = 0
for e, v in equations:
    if is_ok(e, v, True):
        score += e

print(score)
