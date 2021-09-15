import sys
from collections import deque

def make1():
    N = int(sys.stdin.readline())
    memo = [0] * (N + 1)
    for i in range(N + 1):
        if i == 0 or i == 1:
            continue
        elif i == 2 or i == 3:
            memo[i] = 1
        elif not memo[i]:
            if not i%3 and not i%2:
                if memo[i - 1] < memo[i // 2] and memo[i - 1] < memo[i // 3]:
                    memo[i] = memo[i - 1] + 1
                elif memo[i // 2] < memo[i // 3]:
                    memo[i] = memo[i // 2] + 1
                else:
                    memo[i] = memo[i // 3] + 1
            elif not i%3:
                if memo[i - 1] < memo[i // 3]:
                    memo[i] = memo[i - 1] + 1
                else:
                    memo[i] = memo[i // 3] + 1
            elif not i%2:
                if memo[i - 1] < memo[i // 2]:
                    memo[i] = memo[i - 1] + 1
                else:
                    memo[i] = memo[i // 2] + 1
            else:
                memo[i] = memo[i - 1] + 1
    print(memo[i])
    return


def Countfac0():
    N = int(sys.stdin.readline())
    cnt = 0
    i=1
    while N//(5**i):
        cnt += N//(5**i)
        i+=1
    print(cnt)
    return


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


def bfs2(arr):
    dx = [1, 0, -1, 0, 1, 1, -1, -1]
    dy = [0, -1, 0, 1, 1, -1, 1, -1]
    que = deque()
    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j]:
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
            break
        maps = [[0] * (w + 2)]
        for i in range(h):
            maps.append([0] + list(map(int, sys.stdin.readline().split())) + [0])
        maps.append([0] * (w + 2))
        t = bfs2(maps)
        print(t)


island()
