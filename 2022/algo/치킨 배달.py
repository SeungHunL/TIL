import sys


def select(arr):
    global ans
    if len(arr) == M:
        anslist = []
        for i in arr:
            anslist.append(rot_dist[i])
        anslist=list(map(list,zip(*anslist)))
        ans = min(ans, sum(list(map(min, anslist))))
        return
    else:
        if arr:
            start = arr[-1]
        else:
            start = -1
        for i in range(start + 1, chicken):
            arr.append(i)
            select(arr)
            arr.pop()


input = sys.stdin.readline
N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
house = [[], [], []]
for i in range(N):
    for j in range(N):
        if maps[i][j]:
            house[maps[i][j]].append((i, j))
dist = [[] for _ in range(len(house[1]))]
for i in range(len(house[1])):
    y, x = house[1][i]
    for cy, cx in house[2]:
        dist[i].append((abs(cy - y) + abs(cx - x)))
rot_dist=list(map(list,zip(*dist)))
ans = 1e9
chicken = len(house[2])
select([])
print(ans)
