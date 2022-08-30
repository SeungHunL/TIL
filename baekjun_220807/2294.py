import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
for i in range(n):
    coins.append(int(input()))
coins=list(set(coins))
coins.sort()

dp = [10001] * (k+1)
dp[0]=0

for c in coins:
    for i in range(c,k +1):
        dp[i]=min(dp[i-c]+1,dp[i])
if dp[k]==10001:
    print(-1)
else:
    print(dp[k])