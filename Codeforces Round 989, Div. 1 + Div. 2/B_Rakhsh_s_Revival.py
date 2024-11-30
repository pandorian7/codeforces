t = int(input())
import math

def testcase():
    n, m, k = map(int, input().split())
    s = input()
    i = 0
    consec_weak = 0
    n_times = 0
    while(i<n):
        if s[i]=='0':
            consec_weak += 1
        else:
            consec_weak = 0

        if consec_weak == m:
            consec_weak = 0
            n_times += 1
            i += k
        else:
            i+=1
    print(n_times)


for _ in range(t):
    testcase()