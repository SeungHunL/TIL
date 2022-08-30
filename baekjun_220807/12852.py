import sys

input = sys.stdin.readline

N=int(input())

dp=[2e9]*(N+1)
dp[1]=1
l=[[]]*(N+1)
l[1]=[1]
for i in range(1,N):
    if i*3<=N:
        if dp[i*3]>dp[i]+1:
            dp[i*3]=dp[i]+1
            l[i*3]=l[i]+[i*3]
    if i*2<=N:
        if dp[i*2]>dp[i]+1:
            dp[i*2]=dp[i]+1
            l[i*2]=l[i]+[i*2]
    if i+1<=N:
        if dp[i+1]>dp[i]+1:
            dp[i+1]=dp[i]+1
            l[i+1]=l[i]+[i+1]
print(dp[-1]-1)
print(' '.join(list(map(str,l[-1][::-1]))))