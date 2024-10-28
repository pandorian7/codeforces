def testcase():
    n = int(input())
    A = list(map(int, input().split()))

    spaces = list()
    spaceMap = dict()
    for i in range(n-1):
        diff = A[i+1] - A[i]
        if not spaceMap.get(diff):
            spaces.append(A[i+1] - A[i])
            spaceMap[diff] = True
    spaces.sort()
    if not len(spaces):
        spaces.append(1)
    
    for space in spaces:
        freepass_used = False
        failed = False
        i = 0
        while(i<n):
            current = A[i]
            nxt = A[i+1] if i+1 < n else current + space
            if (nxt<=current+space):
                i += 2
            else:
                if freepass_used:
                    failed = True
                    break
                else:
                    freepass_used = True
                    i += 1
        if not failed:
            break
        
    print(space)

t = int(input())

for _ in range(t):
    testcase()