import sys
input = sys.stdin.readline
for t in range(int(input())):
    N= int(input())

    dp=[0,1,1,1,2,2,3,4,5]
    if N>8:
        for i in range(9,N+1):
            dp.append(dp[-1]+dp[-5])
    print(dp[N])