import sys

N = int(sys.stdin.readline())
mx = 0
for i in range(N):
    m = N
    count = 0
    stack = []
    while 1:
        n -=  i
        if n < 0:
            break
        stack.append(n)
        i = m - n
        count += 1
    if mx < count:
        mx = count
        mx_i = i
        mstack = stack
