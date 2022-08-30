import sys
input = sys.stdin.readline
for __ in range(int(input())):
    N,K=map(int,input().split())
    ts=[0]+list(map(int,input().split()))
    gcnt=[0]*(N+1)
    board=[[]for _ in range(N+1)]

    for i in range(K):
        a,b=map(int,input().split())
        board[a].append(b)
        gcnt[b]+=1
    T=int(input())
    dp=[0]*(N+1)
    nex=[]
    for i in range(1,N+1):
        if gcnt[i]==0:
            dp[i]=ts[i]
            nex.append(i)
    while nex:
        i = nex.pop()
        for j in board[i]:
            gcnt[j]-=1
            if dp[j]>0:
                dp[j]=max(dp[j],dp[i]+ts[j])
            else:
                dp[j]=dp[i]+ts[j]
            if gcnt[j]==0:
                nex.append(j)
    print(dp[T])
