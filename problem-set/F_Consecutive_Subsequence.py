n = int(input())

numbers = list(map(int, input().split()))

longest = {}

for num in numbers:
    longest[num] = longest.get(num-1, 0) + 1

val, length = max(longest.items(), key=lambda it:it[1])
backwords = []
print(length)
for index, i in enumerate(numbers[::-1]):
    if i == val:
        backwords.append(n-index)
        val -= 1

for i in backwords[::-1]:
    print(i, end=" ")