import sys

N, M = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))
mx = 0
for i in range(N):
    total = 0
    for j in range(i+1, N):
        for k in range(j+1, N):
            total = s[i] + s[j] + s[k]
            if mx < total <= M:
                mx = total
print(mx)