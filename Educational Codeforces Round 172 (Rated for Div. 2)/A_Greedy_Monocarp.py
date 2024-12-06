t = int(input())

def testcase():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    res = []
    for i in range(1, n+1 ):
        val = -(sum(a[:i])-k)
        if val>=0:
            res.append(val)
    print(min(res))

for _ in range(t):
    testcase()