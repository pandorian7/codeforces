from itertools import count

a, b = map(int, input().split())
for i in count(1):
    a, b = a*3, b*2
    if a > b:
        print(i)
        break