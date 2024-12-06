t = int(input())

def testcase():
    n = int(input())
    a = list(map(int, input().split()))
    ones = a.count(1)
    twos = a.count(2)
    twos = twos%2
    if ones%2==0:
        if twos==1:
            if ones>=2:
                return 1
            else:
                return 0
        return 1
    return 0

for _ in range(t):
    res = testcase()
    print("YES" if res else "NO")