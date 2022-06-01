import sys

input = sys.stdin.readline


def multi(a, b, c):
    if b == 1:
        return a % c
    else:
        tmp = multi(a, b // 2,c)
        if b % 2:
            return (tmp * tmp * a) % c
        else:
            return (tmp * tmp) % c


A, B, C = map(int, input().split())
print(multi(A, B, C))
