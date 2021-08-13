import sys

M = int(sys.stdin.readline())
N = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
O = map(int, sys.stdin.readline().split())
print(O)
for i in range(K):
    if O[i] in N:
        O[i] = 1
    else:
        O[i] = 0
for j in range(K):
    print(O[i],end=" ")
