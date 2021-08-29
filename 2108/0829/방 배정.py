import sys

N, K = map(int, sys.stdin.readline().split())
stack = [[0, 0] for __ in range(6)]
for _ in range(N):
    s, g = map(int, sys.stdin.readline().split())
    stack[g - 1][s] += 1
ans = 0
for i in range(6):
    for j in range(2):
        ans += stack[i][j] // K
        if stack[i][j] % K:
            ans += 1
print(ans)
