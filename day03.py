import re

with open("input03.txt") as i:
    input = i.read()

test_data = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
# input = test_data_2

muls = re.findall(r"mul\(\d+,\d+\)", input)

def parse_mul(m: str):
    x, y = re.match(r"mul\((\d+),(\d+)\)", m).groups()
    return int(x)*int(y)

tmp = [parse_mul(x) for x in muls]
print(sum(tmp))

test_data_2 = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
# input = test_data_2

parts = re.split(r"(do\(\)|don't\(\))", input)

res = []
i = 0
adding = True
while i<len(parts):
    if parts[i] == "don't()":
        adding = False
    elif parts[i] == 'do()':
        adding = True
    elif adding:
        res.extend(re.findall(r"mul\(\d+,\d+\)", parts[i]))
    i += 1


tmp = [parse_mul(x) for x in res]
print(sum(tmp))
