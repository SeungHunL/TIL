import sys


N = int(sys.stdin.readline())
l = [0] * 10001
for _ in range(N):
    l[int(sys.stdin.readline())] += 1
for __ in range(10001):
    if l[__] != 0:
        for i in range(l[__]):
            print(__)
