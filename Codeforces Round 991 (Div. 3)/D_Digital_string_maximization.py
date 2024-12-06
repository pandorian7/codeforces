t = int(input())

def optimize_digits(s):
    # Convert string to list of integers
    digits = list(map(int, s))
    n = len(digits)
    
    # Use a single pass approach instead of nested loops
    i = 1
    while i < n:
        # Check if we can optimize by looking at previous digit
        if i > 0 and digits[i-1] < digits[i]-1 and digits[i] != 0:
            # Perform the swap and decrement
            digits[i-1], digits[i] = digits[i]-1, digits[i-1]
            # Move back one position to check if more optimizations are possible
            i = max(1, i-1)
        else:
            i += 1
    
    # Convert back to string and return
    return "".join(map(str, digits))

def testcase():
    s = input()
    # digs = list(map(int, s))
    # for i in range(len(digs)):
    #     for j in range(1, len(digs)):
    #         d1 = digs[j-1]
    #         d2 = digs[j]
    #         if (d1<d2-1 and d2!=0):
    #             digs[j], digs[j-1] = digs[j-1], digs[j]-1
    print(optimize_digits(s))
    # print("".join(map(str, digs)))

for _ in range(t):
    testcase()