with open("input05.txt") as i:
    input = [x.strip() for x in i.readlines()]

# 75,97,47,61,53

test_data = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""".split("\n")

# input = test_data

rules: dict[str,list[str]] = {}
reverse_rules: dict[str,list[str]] = {}
i = 0
while i<len(input):
    line = input[i]
    if line == "":
        break
    a, b = line.split("|")
    tmp = rules.get(a, [])
    tmp.append(b)
    rules[a] = tmp

    tmp = reverse_rules.get(b, [])
    tmp.append(a)
    reverse_rules[b] = tmp
    i += 1

i += 1

def is_in_correct_order(values: list, rules: dict[str, str]) -> bool:
    for i in range(0, len(values)):
        if values[i] not in values:
            continue

        allowed = rules.get(values[i], None)
        if allowed is None:
            continue
        
        for x in allowed:
            if x in values and values.index(x)<values.index(values[i]):
                return False

    return True

part1 = 0
incorrect_rows = []
while i<len(input):
    line = input[i]
    order = line.split(",")
    if is_in_correct_order(order, rules):
        part1 += int(order[len(order)//2])
    else:
        incorrect_rows.append(order)
    i += 1

print(part1)

def fix_row(values: list[str], reverse_rules: dict[str,list[str]]) -> list[str]:
    result = []

    def handle(value: str):
        tmp = []
        rules = [x for x in reverse_rules.get(value,[]) if x not in result and x in values]
        if len(rules)>0:
            for x in rules:
                tmp2 = handle(x)
                for y in tmp2:
                    if y not in tmp:
                        tmp.append(y)

        tmp.append(value)
        return tmp

    for x in values:
        if x in result:
            continue
        result.extend(handle(x))


    return result

part2 = 0
for row in incorrect_rows:
    r = fix_row(row, reverse_rules)
    part2 += int(r[len(r)//2])

print(part2)