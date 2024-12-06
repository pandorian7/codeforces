from itertools import count

y = int(input())

for i in count(y+1):
    if len(set(str(i))) == 4:
        print(i)
        break

