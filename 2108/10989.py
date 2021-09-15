import sys


def dran(s):
    for _ in range(N):
        s[int(sys.stdin.readline())] += 1
    for __ in range(10001):
        while s[__]:
            print(__)
            s[__] -= 1


N = int(sys.stdin.readline())
l = [0] * 10001
dran(l)
