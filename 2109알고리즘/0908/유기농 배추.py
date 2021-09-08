import sys

for _ in range(int(sys.stdin.readline())):
    M, N, K = map(int, sys.stdin.readline().split())
    land=[[0]*M for __ in range(N)]
    for k in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        land[Y][X]=1
    print(land)