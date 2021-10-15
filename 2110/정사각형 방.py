from collections import deque


def bfs(start, num):
    que = deque()
    que.append(start)
    c = 0
    while que:
        c += 1
        ty, tx = que.popleft()
        for i in range(4):
            ry = ty + dy[i]
            rx = tx + dx[i]
            if 0 <= ry < N and 0 <= rx < N:
                if maps[ry][rx] == maps[ty][tx] + 1:
                    que.append((ry, rx))
    if c not in ans or ans[c]>num:
        ans[c] = num


dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
for q in range(int(input())):
    N = int(input())
    maps = []
    ans = {}
    for i in range(N):
        maps.append(list(map(int, input().split())))
    for j in range(N):
        for k in range(N):
            bfs((j, k), maps[j][k])
    print(f'#{q + 1} {ans[max(ans)]} {max(ans)}')
