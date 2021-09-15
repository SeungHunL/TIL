import sys
from collections import deque


def bfs(arr):
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    que = deque()
    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j]:
                que.append((i, j))
                while que:
                    y,x = que.popleft()
                    for k in range(4):
                        tx = x + dx[k]
                        ty = y + dy[k]
                        if arr[ty][tx]:
                            arr[ty][tx] = 0
                            que.append((ty, tx))
                cnt += 1
    return cnt


def SafeSpace():
    N = int(sys.stdin.readline())
    maps = [[0] * (N + 2)]
    for _ in range(N):
        maps.append([0] + list(map(int, sys.stdin.readline().split())) + [0])
    maps.append([0] * (N + 2))
    mx =0
    mn = 100
    mx_safe = 0
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            if mx < maps[y][x]:
                mx = maps[y][x]
            if mn > maps[y][x]:
                mn = maps[y][x]
    if mx == mn:
        print(1)
        return
    for i in range(mn, mx + 1):
        test = [item[:] for item in maps]
        for m in range(1, N + 1):
            for n in range(1, N + 1):
                if test[m][n] <= i:
                    test[m][n] = 0
        t = bfs(test)
        if t > mx_safe:
            mx_safe = t
    print(mx_safe)

SafeSpace()