import sys

input = sys.stdin.readline

k = int(input())
dp = [0] * (k+2)

day = [[0] for i in range(2)]
for i in range(k):
    t,p=map(int,input().split())
    day[0].append(t)
    day[1].append(p)

m=0
for c in range(1,k+1):
    dp[c]=max(dp[c-1],dp[c])
    tt=c+day[0][c]
    if tt<=k+1:
        dp[tt]=max(dp[c]+day[1][c],dp[tt])
print(max(dp))
