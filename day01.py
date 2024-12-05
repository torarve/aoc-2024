with open("input01.txt") as i:
    input = [x.strip() for x in i.readlines()]

# input = """3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3""".split("\n")

values = [tuple(x.split("   ")) for x in input]

list1 = [int(x) for x,_ in values]
list2 = [int(x) for _, x in values]

distances = [abs(x-y) for x, y in zip(sorted(list1), sorted(list2))]
print(sum(distances))

scores = [x*len([y for y in list2 if x==y]) for x in list1]

# print(scores)
print(sum(scores))