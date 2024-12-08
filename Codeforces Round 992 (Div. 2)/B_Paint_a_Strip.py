from itertools import count

lst = [1]

for i in count(1):
    if len(lst) >= 100000:
        break
    nxt = (len(lst)+1)*2
    lst += [i+1]*(nxt-len(lst))

t = int(input())
for _ in range(t):
    i = int(input())
    print(lst[i-1])