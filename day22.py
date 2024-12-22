with open("input22.txt") as i:
    input = [x.strip() for x in i.readlines()]

test_data = """1
10
100
2024""".split("\n")

#input = test_data

initial_secrets = [int(x) for x in input]

# Part 2:
# initial_secrets = [1, 2, 3, 2024]

def next_secret(secret: int) -> int:
    a = secret*64
    a = (a ^ secret)%16777216
    a = a^ (a//32)
    a = a % 16777216
    a = a ^ (a*2048)
    a = a % 16777216
    return a

part1 = 0
all_diffs = []
all_secrets = []
for s in initial_secrets:
    secrets = [s]
    tmp = s
    for i in range(2000):
        tmp = next_secret(tmp)
        secrets.append(tmp)
    part1 += tmp
    diffs = [secrets[i]%10-secrets[i-1]%10 for i in range(1, len(secrets))]
    all_diffs.append(diffs)
    all_secrets.append(secrets[1:])

print(part1)

range_count = {}
for d, s in zip(all_diffs, all_secrets):
    seen = set()
    for i in range(len(d)-4):
        r = tuple(d[i:i+4])
        if not r in seen:
            range_count[r] = range_count.get(r,0) + s[i+3]%10
        seen.add(r)

print(max(range_count.values()))
