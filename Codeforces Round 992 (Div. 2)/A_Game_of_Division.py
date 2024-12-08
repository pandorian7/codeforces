t = int(input())

def testcase():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        res = []
        for j in range(n):
            if i==j:
                continue
            res.append(abs(a[i]-a[j])%k!=0)
        if all(res):
            return i+1
    return -1
            

for _ in range(t):
    res = testcase()
    if res != -1:
        print('YES')
        print(res)
    else:
        print('NO')