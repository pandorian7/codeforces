t = int(input())

def testcase():
    n = int(input())
    a = list(map(int, input().split()))
    a_min = min(a)
    a_max = max(a)

    i_min = a.index(a_min)
    i_max = a.index(a_max)

    min_max = abs(i_min-i_max)

    c, d = (i_min, n-i_max) if i_min<i_max else (i_max, n-i_min)
    c+=1
    return min(c+min_max, d+min_max, c+d)

    

for _ in range(t):
    res = testcase()
    print(res)