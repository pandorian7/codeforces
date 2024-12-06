n = int(input())
a = map(int, input().split())

dp = [0] * int(1e5 + 1)
cnt = [0] * int(1e5 + 1)

for ai in a:
    cnt[ai] += 1


dp[1] = cnt[1]


for i in range(2, int(1e5)+1):
    dp[i] = max(dp[i-1], dp[i-2]+i*cnt[i])

print(dp[int(1e5)])