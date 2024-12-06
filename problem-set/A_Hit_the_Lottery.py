n = int(input())

notes = [100, 20, 10, 5, 1]

min_notes = 0

for i in notes:
    min_notes += n // i
    n %= i

print(min_notes)