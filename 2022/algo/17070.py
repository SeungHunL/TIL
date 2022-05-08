import sys
from collections import deque
def simulation():
    que=deque()
    que.append((0,1,0))
    route[0][1]=1
    while que:
        y,x,d=que.popleft()
        if d==0:
            if x+1<N and not maps[y][x+1]:
                route[y][x+1][+=route[y][x]
                que.append((y,x+1,0))
            if x+1<N and y+1<N and not maps[y+1][x+1]:
                route[y+1][x + 1] += route[y][x]
                que.append((y+1, x + 1, 1))
        if d==1:
            if x+1<N and not maps[y][x+1]:
                route[y][x+1]+=route[y][x]
                que.append((y,x+1,0))
            if x+1<N and y+1<N and not maps[y+1][x+1]:
                route[y+1][x + 1] += route[y][x]
                que.append((y+1, x + 1, 1))
            if y+1 < N and not maps[y+1][x]:
                route[y + 1][x] += route[y][x]
                que.append((y + 1, x, 2))
        if d==2:
            if x+1<N and y+1<N and not maps[y+1][x+1]:
                route[y+1][x + 1] += route[y][x]
                que.append((y+1, x + 1, 1))
            if y+1 < N and not maps[y+1][x]:
                route[y + 1][x] += route[y][x]
                que.append((y + 1, x, 2))
input = sys.stdin.readline

N = int(input())
maps=[]
for i in range(N):
    maps.append(list(map(int,input().split())))
route=[[[0,0,0]]*N for _ in range(N)]
simulation()
print(route[-1][-1])
for r in route:
    print(r)