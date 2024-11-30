import math

# t = int(input())

UP = 'U'
DOWN = 'D'
LEFT = 'L'
RIGHT = 'R'
UNK = '?'

def get_ith_ring(n, m,i ):
    ul = i, i
    ur = m-1-i, i
    dl = i, n-1-i
    dr = m-1-i, n-1-i
    return ul, ur, dl, dr

def top(i, m, n):
    ul, ur, dl, dr = get_ith_ring(n, m, i)
    points = []
    for j in range(ul[0], ur[0]+1):
        points.append((j, ul[1]))
    return points

def bottom(i, m, n):
    ul, ur, dl, dr = get_ith_ring(n, m, i)
    points = []
    for j in range(dl[0], dr[0]+1):
        points.append((j, dl[1]))
    return points

def left(i, m, n):
    ul, ur, dl, dr = get_ith_ring(n, m, i)
    points = []
    for j in range(ul[1], dl[1]+1):
        points.append((ul[0], j))
    return points

def right(i, m, n):
    ul, ur, dl, dr = get_ith_ring(n, m, i)
    points = []
    for j in range(ur[1], dr[1]+1):
        points.append((ur[0], j))

    return points

def all_cells(n,m):
    for i in range(n):
        for j in range(m):
            yield i, j

def points_in_ring(i, m, n):
    return[*top(i, m, n), *right(i, m, n)[1:-1], *bottom(i, m, n)[::-1], *left(i, m, n)[1:-1][::-1]]

def n_rings(n, m):
    return math.ceil(min(n, m)/2)

def testcase():
    n, m = int(input().split())
    p_map = [[ch for ch in input()] for _ in range(n)]

    n_r = n_rings(n, m)
    

# for _ in range(t):
#     testcase()

n, m = 10, 12
print(points_in_ring(0, m, n))