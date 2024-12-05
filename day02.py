with open("input02.txt") as i:
    input = [x.strip() for x in i.readlines()]

test_data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""".split("\n")


# input = test_data

def parse_rule(rule: str) -> list[int]:
    return [int(x) for x in rule.split(" ")]


def is_safe(levels: list[int]) -> bool:
    diffs = []
    for i in range(0, len(levels)-1):
        diffs.append(levels[i+1]-levels[i])

    if diffs[0] < 0:
        diffs = [-x for x  in diffs]
    
    if any([x < 0 for x in diffs]):
        return False
    
    if any([ x < 1 or x > 3 for x in diffs]):
        return False
    
    return True
    
def is_safe_2(levels: list[int]) -> bool:
    if is_safe(levels):
        return True
    
    for i in range(0, len(levels)):
        if is_safe(levels[:i]+levels[i+1:]):
            return True

    return False

safe_count = 0
safe_count_2 = 0
for rule in input:
    levels = parse_rule(rule)
    
    if is_safe(levels):
        safe_count += 1

    if is_safe_2(levels):
        safe_count_2 += 1


print(safe_count)
print(safe_count_2)
