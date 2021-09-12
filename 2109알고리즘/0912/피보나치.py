import sys


def fib(n):
    if n == 0:
        cnt[0] += 1
        return 0
    elif n == 1:
        cnt[1] += 1
        return 0
    else:
        return fib(n - 1) + fib(n - 2)


for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    cnt = [0, 0]
    fib(N)
    print(cnt[0], end=' ')
    print(cnt[1])
