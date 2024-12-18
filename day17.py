import re


with open("input17.txt") as i:
    input = [x.strip() for x in i.readlines()]

test_data = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0""".split("\n")

# input = test_data

a, b, c = 0, 0, 0
program = None

for l in input:
    if l.startswith("Register "):
        r, v = re.match(r"Register (A|B|C): (\d+)", l).groups()
        if r == "A": a = int(v)
        elif r == "B": b = int(v)
        elif r == "C": c = int(v)
    elif l.startswith("Program: "):
        program = [int(x) for x in l[9:].split(",")]

def run_program(program: list[int], aa: int, bb: int, cc: int) -> list[int]:
    output = []
    a, b, c = aa, bb, cc
    ip = 0
    while ip < len(program):
        i = program[ip]
        op = program[ip+1]
        cop = None
        if op == 4: cop = a
        elif op == 5: cop = b
        elif op == 6: cop = c
        else: cop = op

        if i == 0: # adv
            a = a // (2**cop)
        elif i == 1: # bxl
            b = b ^ op
        elif i == 2: #bst
            b = cop % 8
        elif i == 3: # jnz
            if a != 0:
                ip = op
                continue
        elif i == 4: # bxc
            b = b ^ c
        elif i == 5: # out
            output.append(cop%8)
        elif i == 6: # bdv
            b = a // (2**cop)
        elif i == 7: # cdv
            c = a // (2**cop)
        ip += 2
    return output

result = run_program(program, a, b, c)
print(",".join([str(x) for x in result]))

current = len(program)
solutions = [0]
while current>0:
    next_solutions = []
    for aa in solutions:
        for i in range(8):
            r = run_program(program, (aa<<3) | i, b, c)
            if r[0] == program[current-1]:
                next_solutions.append((aa << 3) | i)
    current = current - 1
    solutions = next_solutions

part2 = min(solutions)
print(part2)
