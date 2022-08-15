import sys
input = sys.stdin.readline
for t in range(int(input())):
    N= int(input())
    ss = []
    ss.append(list(map(int,input().split())))
    ss.append(list(map(int,input().split())))

    dp = [[0]*N for _ in range(2)]
    dp[0][0],dp[1][0]=ss[0][0],ss[1][0]
    if N>=2:
        dp[0][1], dp[1][1] = max(dp[0][0],ss[1][0]+ss[0][1]), max(dp[1][0],ss[0][0]+ss[1][1])
    if N>=3:
        for i in range(2,N):
            dp[0][i] = max( dp[0][i-1],dp[0][i-2]+ss[0][i],dp[1][i-1]+ss[0][i] )
            dp[1][i] = max( dp[1][i-1],dp[1][i-2]+ss[1][i],dp[0][i-1]+ss[1][i] )
    print(max(dp[0][-1],dp[1][-1]))