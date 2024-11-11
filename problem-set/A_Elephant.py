x = int(input())
steps = 0

for i in [5, 4, 3, 2, 1]:
    steps += x // i
    x %= i

print(steps)