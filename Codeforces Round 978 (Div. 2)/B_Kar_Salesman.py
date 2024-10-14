import math

t = int(input())
    
def reduce(a, x):
    a = [i-1 for i in a[:x]] + a[x:]
    a = [i for i in a if i != 0]
    return a 
    
    
def testcase_old():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    n_customers = 0
    while(len(a)):
        a.sort(reverse=True)
        n_customers += 1
        a = reduce(a, x)
    print(n_customers)
    
def testcase():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(max(max(a), math.ceil(sum(a)/x)))
    
for i in range(t):
    testcase()