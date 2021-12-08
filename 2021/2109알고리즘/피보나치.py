import sys

memo = {0: (1, 0), 1: (0, 1)}


def fib(n):
    if n in memo:
        cnt[0] += memo[n][0]
        cnt[1] += memo[n][1]
    else:
        if n-1 in memo and n-2 in memo:
            memo[n] = (memo[n-1][0]+memo[n-2][0],memo[n-1][1]+memo[n-2][1])
        fib(n-1)
        fib(n-2)


for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    cnt = [0, 0]
    fib(N)
    print(cnt[0], end=' ')
    print(cnt[1])
