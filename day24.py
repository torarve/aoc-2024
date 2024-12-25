import operator
from pprint import pprint
import re


with open("input24.txt") as i:
    input = [x.strip() for x in i.readlines()]

test_data_1 = """x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02""".split("\n")

test_data_2 = """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj""".split("\n")

# input = test_data_1
# input = test_data_2

wires = {}
i = 0
while input[i]!="":
    n, v = input[i].split(": ")
    wires[n] = int(v)
    i += 1

operator_lookup = { "AND": operator.and_, "OR": operator.or_, "XOR": operator.xor }

gates = {}
for l in input[i+1:]:
    l, op, r, o = re.match(r"(.+) (AND|OR|XOR) (.+) -> (.+)", l).groups()
    gates[o] = (l, operator_lookup[op], r)

def get_bit(name: str) -> int:
    if name in wires.keys():
        return wires[name]
    l, op, r = gates[name]
    res =  op(get_bit(l), get_bit(r))
    return res

bit_count = max([int(x[1:]) for x in gates.keys() if x.startswith("z")])+1

res = 0
for i in range(bit_count-1,-1, -1):
    b = get_bit(f"z{i:02}")
    res = (res<<1) | b

print(res)


def swap_gates(a, b):
    t = gates[a]
    gates[a] = gates[b]
    gates[b] = t


def add(a: int, b: int) -> int:
    for i in range(bit_count):
        wires[f"x{i:02}"] = (a>>i)%2
        wires[f"y{i:02}"] = (b>>i)%2

    res = 0
    try:
        for i in range(bit_count-1,-1, -1):
            c = get_bit(f"z{i:02}")
            res = (res<<1) | c
    except RecursionError:
        raise "Loop detected"
    return res


def find_gate(a, op, b):
    for k, v in gates.items():
        aa, opp, bb = v
        if ((a==aa and b==bb) or (a==bb and b==aa)) and opp==op:
            return k
        
    return None
        
def find_gate2(a, op):
    for k, v in gates.items():
        if (v[0]==a or v[2]==a) and op==v[1]:
            return k

print()

# f[i] = x[i] xor y[i]
# g[i] = x[i] and y[i]

# z[i] = (x[i] xor y[i]) xor r[i-1]
# z[i] = f[i] xor r[i-1]

# r[i] = (x[i] and y[i]) or ((x[i] xor y[i]) and r[i-1])
# r[i] = g[i] or (f[i] and r[i-1])

remainders = [find_gate("x00", operator.and_, "y00")]
f = [find_gate(f"x{i:02}", operator.xor, f"y{i:02}") for i in range(0, bit_count)]
g = [find_gate(f"x{i:02}", operator.and_, f"y{i:02}") for i in range(0, bit_count)]

swaps = []
for i in range(1, bit_count-1):
    e = find_gate2(f[i], operator.xor)
    if e is not None and e!=f"z{i:02}":
        swaps.append((e, f"z{i:02}"))
    elif e is None:
        print(f"No swap found for bit {i}...")
        # e = find_gate2(remainders[i-1], operator.xor)
        # print(e)
        # print(remainders)
        # swaps.append()

    # x = find_gate2(f[i], operator.and_)
    # rr = find_gate2(g[i], operator.or_)
    # print(x, rr)
    remainders.append(find_gate2(g[i], operator.or_))

print(",".join(sorted([x for y in swaps for x in y])))
