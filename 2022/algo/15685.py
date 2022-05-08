import sys

def curve(x,y,d,l):
    dc=[]
    # 0단계
    dc.append(d)
    for i in range(1,l+1):
        curveLevel = []
        prev=dc[::-1]
        for j in prev:
            curveLevel.append((j+1)%4)
        dc+=curveLevel
    maps[x][y]=1
    for i in dc:
        if i==0:
            x+=1
        elif i==1:
            y-=1
        elif i == 2:
            x-=1
        elif i == 3:
            y+=1
        maps[x][y]=1

input = sys.stdin.readline

N = int(input())
maps=[[0]*101 for _ in range(101)]
for i in range(N):
    x,y,d,l = map(int,input().split())
    curve(x,y,d,l)
prev=[]
answer=0
for i in range(101):
    line = []
    for j in range(101):
        if maps[i][j] and j+1<=100 and maps[i][j+1]:
            if j in prev:
                answer+=1
            line.append(j)
    prev = line[:]
print(answer)

