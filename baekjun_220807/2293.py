import sys

input = sys.stdin.readline

n, k = map(int, input().split())

dp = [[0] * (k + 1) for _ in range(2)]

coins = []
for i in range(n):
    coins.append(int(input()))
coins.sort()

for c in range(n):
    for i in range(k+1):
        if i==0:
            dp[1][0]=1
        elif coins[c] > i:
            dp[1][i] = dp[0][i]
        else:
            dp[1][i] = dp[1][i-coins[c]]+dp[0][i]
    dp[0][:]=dp[1][:]
print(dp[0][-1])
