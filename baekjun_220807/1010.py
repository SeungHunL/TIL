import sys

input = sys.stdin.readline
dp = [0,1]
for i in range(2,31):
    dp.append(dp[-1]*i)

for _ in range(int(input())):
    b,a=map(int,input().split())
    if b==a:
        ans=1
    else:
        ans=dp[a]//(dp[b]*dp[a-b])
    print(ans)