n, h = map(int, input().split())
a = map(int, input().split())

n_standing = n_bent = 0

for ai in a:
    if ai>h:
        n_bent += 1
    else:
        n_standing += 1

print(n_standing + 2*n_bent)