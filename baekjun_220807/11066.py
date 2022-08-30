import sys
input = sys.stdin.readline
for _ in range(int(input())):
    N=int(input())
    ps=list(map(int,input().split()))
    dp=[[0]*(N+1) for _ in range(N+1)]
    for i in range(N-1):
        dp[i][i+1]=ps[i]+ps[i+1]
        for j in range(i+2,N):
            dp[i][j]=dp[i][j-1]+ps[j]


    for v in range(2,N):
        for i in range(N-v):
            j=i+v
            dp[i][j]+=min([dp[i][k]+dp[k+1][j] for k in range(i,j)])
    print(dp[0][N-1])