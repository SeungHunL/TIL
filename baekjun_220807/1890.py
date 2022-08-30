import sys

input = sys.stdin.readline

N=int(input())
board=[]
for i in range(N):
    board.append(list(map(int,input().split())))

ans=[[0]*N for _ in range(N)]
ans[0][0]=1
for i in range(N):
    for j in range(N):
        tmp=board[i][j]
        tmdp=ans[i][j]
        if tmp==0:
            continue
        if i+tmp<N:
            ans[i+tmp][j]+=ans[i][j]
        if j+tmp<N:
            ans[i][j+tmp] += ans[i][j]
print(ans[-1][-1])