n, t = map(int, input().split())
s = input()

for j in range(t):
    indexes = []
    for i in range(len(s)-1):
        if s[i:i+2] == "BG":
            indexes.append(i)
    for i in indexes:
        s = s[:i] + "GB" + s[i+2:]
    if not len(indexes):
        break
print(s)