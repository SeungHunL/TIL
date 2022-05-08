import sys
from collections import deque
input = sys.stdin.readline

x,y = map(int,input().split())
maps = []
d = [(1,0),(0,1),(-1,0),(0,-1)]
for i in range(y):
    line = list(input().split())
    if "B" in line:
        bx = line.index("B")
        by = i
    if "R" in line:
        rx = line.index("B")
        ry = i
    if "O" in line:
        ox = line.index("O")
        oy = i
    maps.append(line)
que = deque()
while 1:
    bx,by,rx,ry=que.popleft()
    for v,h in d:
        if v == 1:
            b = False
            move_b = maps[by][bx+1]
            move_r = maps[ry][rx+1]
            while 1:
                if move_b=="#":
                    break
                elif move_b=="O":
                    b = True
                    break
                else:
                    bx+=1
                if move_r=="#":
                    break
                elif move_r=="O" and not b:
                    # end
                    break
                else:
                    rx+=1
        elif v == -1:
            while (maps[by][bx-1]!="#"):
                    bx-=1
        elif h == 1:
            while (maps[by+1][bx]!="#"):
                    by+=1
        elif h == -1:
            while (maps[by-1][bx]!= "#"):
                    by-=1