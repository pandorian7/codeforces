t = int(input())

def testcase():
    n = int(input())
    a = list(map(int, input().split()))
    m = {0:[], 1:[], 2:[]}
    changes = []
    for i in range(n):
        m[int(a[i])].append(i)

    while (len(m[0]) and len(m[1]) and m[1][0]<m[0][-1]):
        last = m[0].pop(-1)
        first = m[1].pop(0)
        changes.append((last, first))
        m[0].insert(0, first)
        m[1].append(last)

        print(m, changes)

    while (len(m[1]) and len(m[2]) and m[2][0]<m[1][-1]):
        last = m[1].pop(-1)
        first = m[2].pop(0)
        changes.append((last, first))
        m[1].insert(0, first)
        m[2].append(last)

        print(m, changes)

    while (len(m[0]) and len(m[1]) and m[1][0]<m[0][-1]):
        last = m[0].pop(-1)
        first = m[1].pop(0)
        changes.append((last, first))
        m[0].insert(0, first)
        m[1].append(last)

        print(m, changes)

    while (len(m[1]) and len(m[2]) and m[2][0]<m[1][-1]):
        last = m[1].pop(-1)
        first = m[2].pop(0)
        changes.append((last, first))
        m[1].insert(0, first)
        m[2].append(last)

        print(m, changes)
    # while (len(m[1]) and len(m[2]) and m[2][0]<m[1][-1]):
    #     changes.append((m[1].pop(-1), m[2].pop(0)))
    #     m[1].append(changes[-1][1])



for _ in range(t):
    testcase()