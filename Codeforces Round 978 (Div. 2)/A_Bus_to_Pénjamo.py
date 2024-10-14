t = int(input())

def testcase():
    n, r = map(int, input().split())
    a = list(map(int, input().split()))
    n_happy = 0
    for i, ai in enumerate(a):
        n_rows = ai//2
        r -= n_rows
        n_together = n_rows*2
        n_happy += n_together
        a[i] = ai-n_together   
    rest = sum(a)
    overflow = rest-r
    if overflow > 0:
        n_happy += rest-overflow*2
    else:
        n_happy += rest
    print(n_happy)
        


for _ in range(t):
    testcase()