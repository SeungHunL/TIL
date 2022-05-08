# 6 3 15
# 0 0 1 0 0 0
# 0 0 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 1 0
# 0 0 0 1 0 0
# 6 5
# 2 2 5 6
# 5 4 1 6
# 4 2 3 5
import sys
from collections import deque
d=[(1,0),(-1,0),(0,1),(0,-1)]
def drive(start,end):
    que=deque()
    nque= deque()
    que.append(start)
    nmap= [item[:] for item in maps]
    for i in guests:
        nmap[i[0]][i[1]]=2
    while que:
        y,x = que.popleft()
        nmap[y][x]=3
        for iy,ix in d:
            ty,tx= y+iy,x+ix
            if 0<=ty<N and 0<=tx<N and not nmap[ty][tx]:
                nque.append((ty,tx))
        if not que and nque:
            que=nque
            nque=deque()

input = sys.stdin.readline

N,M,Fuel=map(int,input().split())
maps=[]
for i in range(N):
    maps.append(list(map(int,input().split())))
sy,sx =map(int,input().split())
guests=[]
for i in range(M):
    guests.append(list(map(int,input().split())))

