import math

def testcase():
    x, y, k = map(int, input().split())
    zero = (0, 0)
    A = B = C = D = zero
    
    min_block_length = int(math.ceil(k*math.cos(math.pi/4)))

    B = (min_block_length, min_block_length)

    C = (min_block_length, 0)
    D = (0, min_block_length)

    if (x > y):
        D = (x - min_block_length, min_block_length)
        C = (x, 0)
    if (y > x):
        D = (min_block_length, y - min_block_length)
        C = (0, y)
    
    Ax, Ay = A
    Bx, By = B
    Cx, Cy = C
    Dx, Dy = D

    print(Ax, Ay, Bx, By)
    print(Cx, Cy, Dx, Dy)


t = int(input())

for _ in range(t):
    testcase()