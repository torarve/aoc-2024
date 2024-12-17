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
            # print(cop%8)
        elif i == 6: # bdv
            b = a // (2**cop)
        elif i == 7: # cdv
            c = a // (2**cop)
        ip += 2
    return output

result = run_program(program, a, b, c)
print(",".join([str(x) for x in result]))



# result = run_program(program, 117440, b, c)
# print(",".join([str(x) for x in result]))
aa = a


def run_program2(program: list[int], aa: int, bb: int, cc: int, expected: list[int]) -> bool:
    output_count = 0
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
            if expected[output_count] != cop%8:
                return False
            output_count += 1
            # output.append(cop%8)
            # print(cop%8)
        elif i == 6: # bdv
            b = a // (2**cop)
        elif i == 7: # cdv
            c = a // (2**cop)
        ip += 2
    return True

# program = [0,3,5,4,3,0]
# aa = 2024

# while len(result)!=len(program) or any([a!=b for a,b in zip(result,program)]):
#     aa += 1
#     if aa%1000 == 0: print(aa)
#     # print(aa)
#     result = run_program(program, aa, b, c)

# while not run_program2(program, aa, b, c, program):
#     aa += 1
#     if aa%1000 == 0: print(aa)


# print(result)
# print(run_program(program, aa, b, c))
# print(program)


# 2,4 **  b = a%8 (three lowest bits) 
# 1,1     b = b^1 (flip last bit)
# 7,5     c = a // (2**b) => c = a << b
# 1,5     b = b ^ 5
# 0,3 *   a = a//(2**3) => shift 3 bits
# 4,4     b = b^c
# 5,5 *** out b%8
# 3,0 *   jnz 0

# abc (efg)

# 101

# 6
# 25283264
# program = [0,3,5,4,3,0]
# aa = 2024
# print(aa)
# 2,4,1,1,7,5,1,5,0,3,4,4,5,5,3,0
# for i in range(2**6):
#     r = run_program(program, i, b, c)
#     if r[0] == 2: print(2, bin(i))
#     if len(r)>1 and r[1] == 4: print(4, bin(i))
#     if len(r)>1 and r[0]==2 and r[1]==4: print(bin(i)) 
#     if len(r)>2 and r[0]==2 and r[1]==4 and r[2]==1: print(bin(i)) 
    # if r[0] == 2: print(bin(i))


current = 0
aa = 0
step = 1
# while len(result)!=len(program) or any([a!=b for a,b in zip(result,program)]):
while current<len(program):
    # print(aa + step << (3*current))
    r = run_program(program, aa, b, c)
    if current>=len(r) or r[current]!=program[current]:
        aa += step
    else:
        current += 1
        print(aa, step)
        step = step << 3

# to high: 173389917829966
print(program)
print(r)
print(aa)
# 001 110
# 110
# 6  110
# 14 8+4+2 