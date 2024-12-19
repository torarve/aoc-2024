import functools


with open("input19.txt") as i:
    input = [x.strip() for x in i.readlines()]

test_data = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb""".split("\n")

# input = test_data

available = input[0].split(", ")
patterns = input[2:]

@functools.cache
def count_all(pattern: str) -> bool:
    if len(pattern) == 0: return 1
    count = 0
    for t in available:
        if pattern.startswith(t):
            count += count_all(pattern[len(t):])
    return count


counts = []
for i, p in enumerate(patterns):
    # print(f"{i+1}/{len(patterns)}")
    counts.append(count_all(p))

print(sum([1 if x>0 else 0 for x in counts]))
print(sum(counts))