n = int(input())

ps = [0]

for _ in range(n):
    ai, bi = map(int, input().split())
    ps.append(ps[-1] - ai + bi)

print(max(*ps))