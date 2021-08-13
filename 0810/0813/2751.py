from sys import stdin

N = int(stdin.readline())
l = [0]*N
for _ in range(N):
    l[_] = int(stdin.readline())
l.sort()
for __ in range(N):
    print(l[__])
