import sys

input = sys.stdin.readline

n, m = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(input())
ans=0
nmap = [[0]*m for _ in range(n)]
for i in range(1,len(maps)):
    if maps[i][0]=='1':
        ans=1
        nmap[i][0]= 1
for i in range(len(maps[0])):
    if maps[0][i]=='1':
        ans=1
        nmap[0][i]= 1
for i in range(1,n):
    for j in range(1,m):
        if maps[i][j] == '1':
            nmap[i][j]=min(nmap[i-1][j],nmap[i-1][j-1],nmap[i][j-1])+1
            if nmap[i][j]>ans:
                ans = nmap[i][j]
print(ans**2)
