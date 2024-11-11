n = input()

count = 0

for i in n:
    if i in ['4', '7']:
        count += 1

count = str(count)

if len(count) == count.count('4') + count.count('7'):
    print("YES")
else:
    print("NO")