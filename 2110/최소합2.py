from collections import deque

def bfs(arr):
    s=(0,0)
    que=deque()
    que.append(s)
    ans[0][0]=arr[0][0]
    while que:
        ty,tx=que.popleft()
        for i in range(2):
            ry=ty+dy[i]
            rx=tx+dx[i]
            if ry<N and rx<N and (ry,rx):
                que.append((ry,rx))
                if not ans[ry][rx] or ans[ry][rx]>ans[ty][tx]+arr[ry][rx]:
                    ans[ry][rx]=ans[ty][tx]+arr[ry][rx]

dx=[1,0]
dy=[0,1]

for q in range(int(input())):
    N = int(input())
    board = []
    ans=[[0]*N for l in range(N)]
    for w in range(N):
        board.append(list(map(int, input().split())))
    bfs(board)
    print(f'#{q+1} {ans[-1][-1]}')
