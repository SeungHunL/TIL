import sys

input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)
bank = [[] for _ in range(N + 1)]
for _ in range(N):
    T, P = map(int, input().split())
    if T + _ < N + 1:
        bank[T + _].append((T, P))
for n in range(1, N + 1):
    if dp[n] < dp[n - 1]:
        dp[n] = dp[n - 1]
    for t, p in bank[n]:
        if n - t >= 0:
            if dp[n] < dp[n - t] + p:
                dp[n] = dp[n - t] + p
print(dp[-1])
