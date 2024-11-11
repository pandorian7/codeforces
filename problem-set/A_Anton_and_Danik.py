input()
s = input()

A = s.count('A')
D = s.count('D')

if A > D:
    print("Anton")
elif A < D:
    print("Danik")
else:
    print("Friendship")