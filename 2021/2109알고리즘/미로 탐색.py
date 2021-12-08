import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maz = [[0] * (M + 2)]
for _ in range(N):
    maz.append([0] + list(map(int, list(sys.stdin.readline().strip()))) + [0])
maz.append([0] * (M + 2))

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

que = deque()
que.append((0, 1, 1))
while que:
    t, y, x = que.popleft()
    t += 1
    if (y, x) == (N, M):
        print(t)
        break
    for k in range(4):
        tx, ty = x + dx[k], y + dy[k]
        if maz[ty][tx]:
            maz[ty][tx] = 0
            que.append((t, ty, tx))
