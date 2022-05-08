import sys

input = sys.stdin.readline

n, m = map(int, input().split())
c=0
maps = []
for _ in range(n):
    maps.append(input())
while 1:
    horizonmap = []
    for i in range(n-1):
        h = ''
        for j in range(m - 1):
            if maps[i][j] == '1' and maps[i][j + 1] == '1' and maps[i+1][j] == '1' and maps[i+1][j + 1] == '1':
                h+='1'
            else:
                h+='0'
        horizonmap.append(h)
    m -= 1
    n -= 1
    maps = horizonmap
    for map in maps:
        if '1' in map:
            if c==0:
                c=1
            c+=1
            break
    else:
        break
print(c**2)
