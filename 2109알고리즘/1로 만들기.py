import sys


def mkone(N):
    if N == 1:
        Memo[N] = 0
        return 1
    if Memo[N] != 0:
        return Memo[N]

    if N % 3 == 0:
        Memo[N] = mkone[N//3]+1
    elif N % 2 == 0:
        Memo[N] = mkone[N//2]+1
    else:
        Memo[N] = mkone[N-1]+1


N = int(sys.stdin.readline())
Memo = [0]*(N+1)
print(mkone(N))
