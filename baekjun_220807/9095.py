import sys

input = sys.stdin.readline
for _ in range(int(input())):
    N=int(input())
    dp=[1,1,2,4]
    if N>3:
        for i in range(4,N+1):
            dp.append(dp[i-1]+dp[i-2]+dp[i-3])
    print(dp[N])