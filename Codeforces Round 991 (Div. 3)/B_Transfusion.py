t = int(input())

def testcase():
    n = int(input())
    nums = list(map(int, input().split()))
    l1 = nums[0::2]
    l2 = nums[1::2]
    s1 = sum(l1)
    s2 = sum(l2)
    if s1%len(l1) == 0 and s2%len(l2) == 0 and s1/len(l1) == s2/len(l2) and s1>=0:
        print("YES")
    else:
        print("NO")

for _ in range(t):
    testcase()