import sys
input=sys.stdin.readline

def robot(y,x,heading):
    # 1 현재 위치를 청소
    c=[0]*4
    while y!=0 or x!=0 or y!=N-1 or x!=M-1 :
        maps[y][x]=1

        #2 현재 위치(y,x)에서 heading을 기준으로 왼쪽
        ly = y + dy[(heading - 1) % 4]
        lx = x + dx[(heading - 1) % 4]
        while 1:
            if not maps[ly][lx]:
                heading -= 1  # 왼쪽 방향에 청소 안 한 공간 존재, 회전
                y, x = ly, lx  # 한 칸 전진
                break
            else:
                c[heading]=1
                heading -= 1
            if c=[1,1,1,1]:
                y-=dy[heading]
                x-=dx[heading]

dy=[1,0,-1,0]
dx=[0,1,0,-1]

N,M=map(int,input().split())
r,c,d=map(int,input().split())
maps=[]
for i in range(N):
    maps.append(list(map(int,input().split())))
robot(r,c,d)
