from math import ceil

t = int(input())

def build_number(n, required):
    arr = ["6"] + ["3"] * (n - 1)
    for i in range(int(required)):
        arr[2*i+1] = "6"
    return "".join(arr[::-1])

def testcase():
    n = int(input())

    n_odd = ceil(n/2)
    n_even = n - n_odd
    odd_sum = 3 * (n_odd + 1)
    even_sum = 3 * n_even
    diff = odd_sum - even_sum
    required = diff/3
    available = n_even
    if available < required:
        print(-1)
    else:
        print(build_number(n, required))

for _ in range(t):
    testcase()