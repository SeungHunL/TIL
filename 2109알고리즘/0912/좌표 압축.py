import sys

N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))
Y = sorted(list(set(X)))
ans = {}
for i in range(len(Y)):
    ans[Y[i]] = i
for k in range(N):
    print(ans[X[k]], end=' ')
