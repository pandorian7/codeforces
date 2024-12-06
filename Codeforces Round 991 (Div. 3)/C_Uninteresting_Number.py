t = int(input())

def testcase():
    twos = threes = 0
    sum_ = 0
    s = input()
    for ch in s:
        n = int(ch)
        if n == 2:
            twos += 1
        if n ==3: 
            threes += 1
        sum_ += n
    twos = min(twos,8)    
    threes = min(threes,8)
    mod = sum_%9
    if mod == 0:
        return "YES"
    for i in range(0,twos+1):
        for j in range(0,threes+1):
            if (mod+i*2+j*6)%9 == 0:
                return "YES"
    return "NO"
        

for _ in range(t):
    res = testcase()
    print(res)