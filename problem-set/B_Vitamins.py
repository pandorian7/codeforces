from collections import defaultdict

dp = defaultdict(dict)

vitamins = {
    'A': 1<<0,
    'B': 1<<1,
    'C': 1<<2
}

n = int(input())

drinks = []

for i in range(n):
    cost, v_str  = input().split()
    cost = int(cost)
    vit = sum([vitamins[v] for v in v_str])
    drinks.append((cost, vit))

