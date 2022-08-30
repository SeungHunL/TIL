import sys

input = sys.stdin.readline
N = int(input())
dp=list(map(int, input().split()))
for _ in range(N-1):
    r,g,b=map(int, input().split())
    tmp=[0]*3
    tmp[0]=min(dp[1],dp[2])+r
    tmp[1]=min(dp[0],dp[2])+g
    tmp[2]=min(dp[0],dp[1])+b
    dp=tmp[:]
print(min(dp))


