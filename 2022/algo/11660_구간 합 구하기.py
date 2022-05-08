import sys
input=sys.stdin.readline
n,m = map(int, input().split())
maps=[]
for i in range(n):
    maps.append(list(map(int, input().split())))
calc=[[0]*(n+1) for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        calc[i][j]=sum(maps[i-1][:j])+calc[i-1][j]
for j in range(m):
    x1,y1,x2,y2=map(int, input().split())
    print(calc[x2][y2]-calc[x2][y1-1]-calc[x1-1][y2]+calc[x1-1][y1-1])