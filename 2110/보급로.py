from collections import deque

def bfs(start):
    que=deque()
    que.append(start)
    while que:
        y, x =que.popleft()
        for i in range(4):
            ty = y + d[i][0]
            tx = x + d[i][1]
            if 0 <= ty < N and 0 <= tx < N:
                if cost[ty][tx] > cost[y][x]+maps[y][x]:
                    cost[ty][tx] = cost[y][x]+maps[y][x]
                    que.append((ty,tx))

d=[(1,0),(0,1),(-1,0),(0,-1)]
for q in range(int(input())):
    N=int(input())
    maps=[]
    for e in range(N):
        maps.append(list(map(int,list(input()))))
    cost=[[10000]*N for w in range(N)]
    cost[0][0]=0
    bfs((0,0))
    print(f'#{q + 1} {cost[-1][-1]}')