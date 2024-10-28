t = int(input())

def testcase():
    n, m, r, c = map(int, input().split())
    dist = (n-r)*(m-1)+(m-c)+m*(n-r)
    print(dist)

for _ in range(t):
    testcase()