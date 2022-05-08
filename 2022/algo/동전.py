import sys

input = sys.stdin.readline
for i in range(int(input())):
    answer=0
    coin_num=int(input())
    coin= list(map(int,input().split()))
    cost = int(input())
    dp=[0]*(cost+1)
    dp[0]=1
    for c in coin:
        for j in range(c,cost+1):
            if j-c>=0:
                dp[j]+=dp[j-c]
    print(dp[-1])

