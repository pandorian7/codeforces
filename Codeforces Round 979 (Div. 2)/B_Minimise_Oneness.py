t = int(input())

def testcase_():
    n = int(input())
    f = g = n//2
    if n%2:
        f+=1
    print("0"*f+"1"*g)

def testcase():
    n = int(input())
    if n%2==0:
        zeros = n-1
    else:
        zeros = n
    ones = n - zeros
    print("1"*ones+"0"*zeros)
    

for _ in range(t):
    testcase()