from math import lcm
import math
import re
with open("input13.txt") as i:
    input = [x.strip() for x in i.readlines()]
    # input = i.read().strip()

test_data = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279""".split("\n")# # 

# input = test_data

machines = []
for i in range(len(input)//4 + 1):
    a, b = re.match(r"Button A: X\+(\d+), Y\+(\d+)", input[i*4]).groups()
    c, d = re.match(r"Button B: X\+(\d+), Y\+(\d+)", input[i*4+1]).groups()
    e, f = re.match(r"Prize: X=(\d+), Y=(\d+)", input[i*4+2]).groups()
    machines.append((int(a), int(b), int(c), int(d), int(e), int(f)))

def find_total_cost(machines):
    total_cost = 0
    for bax, bay, bbx, bby, px, py in machines:
        det = bax*bby - bbx*bay
        a = bby*px - bbx*py
        b = -bay*px + bax*py
        if a%det==0 and b%det==0:
            total_cost += 3*a//det + b//det
    return total_cost

print(find_total_cost(machines))

machines = [(bax, bay, bbx, bby, 10000000000000+px, 10000000000000+py) for bax, bay, bbx, bby, px, py in machines]
print(find_total_cost(machines))