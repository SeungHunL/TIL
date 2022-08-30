import sys

def nqueen(n,board,visit):
    global ans

    if n==N:
        ans+=1
        return
    for i in range(N):
        if visit[i]==0:
            for j in range(1,n+1):
                if n-j>=0 and i-j>=0 and board[n-j][i-j]:
                    break
                if n-j>=0 and i+j<N and board[n-j][i+j]:
                    break
            else:
                board[n][i]=1
                visit[i]=1
                nqueen(n+1,board,visit)
                board[n][i] = 0
                visit[i] = 0


input = sys.stdin.readline
N = int(input())
ans=0
maps=[[0]*N for _ in range(N)]
nqueen(0,maps[::],[0]*N)
print(ans)

