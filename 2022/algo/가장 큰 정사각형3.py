import sys

input = sys.stdin.readline

n, m = map(int, input().split())
c=0
maps = []
for _ in range(n):
    maps.append(input())

nmap = []
for i in range(n-1):
    h=[]
    for j in range(m - 1):
        if maps[i][j] == '1' and maps[i][j + 1] == '1' and maps[i+1][j] == '1' and maps[i+1][j + 1] == '1':
            h.append(True)
        else:
            h.append(False)
    nmap.append(h)
else:
    c+=1
m -= 1
n -= 1

while 1:
    maps=[]
    for i in range(n-1):
        h=[]
        for j in range(m - 1):
            if nmap[i][j] == True and nmap[i][j + 1] == True and nmap[i+1][j] == True and nmap[i+1][j + 1] == True:
                h.append(True)
            else:
                h.append(False)
        maps.append(h)
    nmap=maps
    m -= 1
    n -= 1
    print(maps)
    for ni in range(n):
        if '1' in maps[ni]:
            c+=1
            break
    else:
        break
print(c**2)
