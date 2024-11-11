def nxt(direcion, point):
    x, y = point
    # print(direcion)
    match direcion:
        case 'N':
            return (x, y+1)
        case 'S':
            return (x, y-1)
        case 'E':
            return (x+1, y)
        case 'W':
            return (x-1, y)

def solve():
    n, a, b = map(int, input().split())
    stop = (a, b)
    start = (0, 0)
    position = start
    s = input()
    if position == stop:
        return 1
    for i in range(25):
        for ch in s:
            position = nxt(ch, position)
            if position == stop:
                return 1
    return 0


t = int(input())

for _ in range(t):
    solution = solve()
    print("YES" if solution else "NO")