import sys

input = sys.stdin.readline

n, m = map(int, input().split())
c=1
maps = []
for _ in range(n):
    maps.append(input())
while 1:
    horizonmap = []
    for i in range(n):
        h = ''
        for j in range(m - 1):
            if maps[i][j] == '1' and maps[i][j + 1] == '1':
                h+='1'
            else:
                h+='0'
        horizonmap.append(h)
    m -= 1
    nmap = []
    for i in range(n - 1):
        v = ''
        for j in range(m):
            if horizonmap[i][j] == '1' and horizonmap[i + 1][j] == '1':
                v+='1'
            else:
                v+='0'
        nmap.append(v)
    n -= 1
    maps = nmap
    for map in maps:
        if '1' in map:
            if c==0:
                c=1
            c+=1
            break
    else:
        break
print(c**2)
