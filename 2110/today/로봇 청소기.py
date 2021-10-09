import sys
input=sys.stdin.readline
def robot(y,x,heading):
    maps[y][x]=1
    dy=[0,1,0,-1]
    dx=[-1,0,1,0]
    ty = y + dy[heading]
    tx = x + dx[heading]
    c=4
    while c:
        while not maps[ty][tx]:
            maps[ty][tx]=2
            ty += dy[heading]
            tx += dx[heading]
        heading=(heading-1)%4
        c-=1
N,M=map(int,input().split())
r,c,d=map(int,input().split())
maps=[]
for i in range(N):
    maps.append(list(map(int,input().split())))
robot(r,c,d)
