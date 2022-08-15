import sys

input= sys.stdin.readline

N=int(input())
times=[0]*24
dic={}
for i in range(N):
    a,b=map(int,input().split())
    if a==b:
        times[a]+=1
    elif b in dic:
        dic[b].append(a)
    else:
        dic[b] = [a]

dp=[0]*24
for i in range(1,24):
    if i in dic:
        dp[i]=max(dp[max(dic[i])]+1,dp[i-1])
    else:
        dp[i]=dp[i-1]
    dp[i]+=times[i]
print(dp[-1])
# 4
# 1 3
# 3 4
# 4 5
# 5 6