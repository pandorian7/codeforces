s = input()

count = 0

for i, ch in enumerate(s):
    if ch=='A':
        prv = s[:i].count("Q")
        aft = s[i+1:].count("Q")
        count += prv*aft

print(count)