import sys

M = int(sys.stdin.readline())
N = list(map(int, sys.stdin.readline().split()))
K = int(sys.stdin.readline())
O = list(map(int, sys.stdin.readline().split()))
S = sorted(O)
for i in range(K):
    if O[i] in N:
        O[i] = 1
    else:
        O[i] = 0
for j in range(K):
    print(O[j],end=" ")