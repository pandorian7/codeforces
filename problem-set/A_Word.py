s = input()

n_lower = len(list(filter(str.islower, s)))
n_upper = len(list(filter(str.isupper, s)))

action = str.lower if n_lower >= n_upper else str.upper

s = action(s)

print(s)