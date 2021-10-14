from collections import deque

def bfs(start):
    que=deque()
    que.append(start)
    while que:
        y, x =que.popleft()
        high = maps[y][x]
        for i in range(4):
            ty = y + d[i][0]
            tx = x + d[i][1]
            if 0 <= ty < N and 0 <= tx < N:
                if maps[ty][tx] > high:
                    pay = maps[ty][tx] - high + 1
                else:
                    pay = 1
                if cost[ty][tx] > pay+cost[y][x]:
                    cost[ty][tx] = pay+cost[y][x]
                    que.append((ty,tx))

d=[(1,0),(0,1),(-1,0),(0,-1)]
for q in range(int(input())):
    N=int(input())
    maps=[]
    for e in range(N):
        maps.append(list(map(int, input().split())))
    cost=[[10000]*N for w in range(N)]
    cost[0][0]=0
    bfs((0,0))
    print(f'#{q + 1} {cost[-1][-1]}')
