import sys
from collections import deque

def bfs2(arr):
    dx = [1, 0, -1, 0, 1, 1, -1, -1]
    dy = [0, -1, 0, 1, 1, -1, 1, -1]
    que = deque()
    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j]:
                arr[i][j]=0
                que.append((i, j))
                while que:
                    y, x = que.popleft()
                    for k in range(8):
                        tx = x + dx[k]
                        ty = y + dy[k]
                        if arr[ty][tx]:
                            arr[ty][tx] = 0
                            que.append((ty, tx))
                cnt += 1
    return cnt


def island():
    while 1:
        w, h = map(int, sys.stdin.readline().split())
        if (w, h) == (0, 0):
            return
        maps = [[0] * (w + 2)]
        for i in range(h):
            maps.append([0] + list(map(int, sys.stdin.readline().split())) + [0])
        maps.append([0] * (w + 2))
        t = bfs2(maps)
        print(t)


island()
