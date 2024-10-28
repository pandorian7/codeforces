t = int(input())

def testcase():
    n = int(input())
    a = list(map(int, input().split()))
    min = max = a[0]
    for val in a:
        if (val<min):
            min = val
        if (val>max):
            max = val
    head = max
    sigma_b = head + min*(n-1)
    sigma_c = head + max*(n-1)
    score = sigma_c - sigma_b
    print(score)



for i in range(t):
    testcase()