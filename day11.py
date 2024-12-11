import functools


with open("input11.txt") as i:
    input = i.read().strip()

test_data = """125 17"""

# input = test_data

current = [int(x) for x in input.split(" ")]


def blink(current):
    tmp = []
    for i in current:
        if i == 0:
            tmp.append(1)
        elif len(str(i))%2 == 0:
            x = str(i)
            a, b = x[:len(x)//2], x[len(x)//2:]
            tmp.append(int(a))
            tmp.append(int(b))
        else:
            tmp.append(i*2024)
    return tmp

for i in range(25):
    current = blink(current)

print(len(current))

current = [int(x) for x in input.split(" ")]

@functools.cache
def split_stone(stone: int, steps: int) -> int:
    if steps == 0: return 1

    if stone == 0:
        return split_stone(1, steps-1)
    elif len(str(stone))%2 == 0:
        x = str(stone)
        a, b = x[:len(x)//2], x[len(x)//2:]
        return split_stone(int(a), steps-1) + split_stone(int(b), steps-1)
    else:
        return split_stone(stone*2024, steps-1)
    

print(sum([split_stone(x, 75) for x in current]))