from itertools import combinations

n = int(input())

vitamins = {
    'A': 1<<0,
    'B': 1<<1,
    'C': 1<<2
}

drinks = []

def combs():
    for i in range(1, len(drinks)+1):
        for comb in combinations(drinks, i):
            yield comb

for _ in range(n):
    cost, v_str = input().split()
    cost = int(cost)
    v_val = sum(map(lambda v:vitamins[v], v_str))
    drinks.append((cost, v_val))

costs = []

def OR(vals):
    ret = 0
    for val in vals:
        ret |= val
    return ret

for comb in combs():
    cost_lst, v_lst = zip(*comb)
    cost = sum(cost_lst)
    vs = OR(v_lst)
    if vs==7:
        costs.append(cost)

print(min(costs) if len(costs) else -1)