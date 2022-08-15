import sys
from collections import deque


# def bfs(num):
#     d=[(1,0),(0,1),(-1,0),(0,-1)]
#     que = deque(list(num))
#     while que:
#         que.pop
#         y,x =
#         if

input = sys.stdin.readline
R, C = map(int, input().split())
maps = []
for _ in range(R):
    maps.append(list(input().strip()))
N = int(input())
order = list(map(int, input().split()))
print(maps)
for i in range(N):
    if i % 2 == 0:
        dir = 0
    else:
        dir = -1
    for j in range(C):
        print(i)
        if maps[-order[i]][dir]=='x':
            maps[-order[i]][dir]='.'
            break
        if dir >= 0:
            dir += 1
        else:
            dir -= 1
for m in maps:
    print(m)

# for m in maps:
#     print(m)
