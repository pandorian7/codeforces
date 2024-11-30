from itertools import count

t = int(input())

def testcase():
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    for i in count(1):
        possible_mc = i * a
        if possible_mc%b==0:
            print(possible_mc)
            return

for _ in range(t):
    testcase()