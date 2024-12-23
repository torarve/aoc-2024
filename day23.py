import itertools
from pprint import pprint


with open("input23.txt") as i:
    input = [x.strip() for x in i.readlines()]

test_data = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn""".split("\n")

# input = test_data

nodes: set[str] = set()
edges: tuple[str,str] = set()
for l in input:
    a, b = l.split("-")
    nodes.update([a, b])
    edges.add((a,b))
    edges.add((b,a))

# print(nodes)
# print(edges)

result = set()
for a, b, c in itertools.combinations(nodes, 3):
    if (a, b) in edges and (a,c) in edges and (b, c) in edges:
        result.add(tuple(sorted([a,b,c])))

count = 0
for a, b, c in result:
    if a.startswith("t") or b.startswith("t") or c.startswith("t"):
        count+=1
print(count)

cliques = []
best_clique: set[str] = set()

def BronKerbosch1(R: set[str], P: set[str], X: set[str]) -> set[str]:
    if len(P)==0 and len(X)==0:
        cliques.append(R)
        return R
    pp = set(P)
    best = set()
    for v in P:
        N = set([b for a,b in edges if a==v])
        res = BronKerbosch1(R.union([v]), pp.intersection(N), X.intersection(N))
        if len(res)>len(best):
            best = res
        pp.remove(v)
        X.union([v])
    return best


result = BronKerbosch1(set(), set(nodes), set())

pwd = ",".join([str(x) for x in sorted(result)])
print(pwd)