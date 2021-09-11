import sys
from collections import deque


def bfs(arr,target):
    while target:
        y, x = target.popleft()
        for k in range(4):
            tx, ty = x + dx[k], y + dy[k]
            if not arr[ty][tx] and (ty, tx) not in target:
                arr[ty][tx] = 2
                target.append((ty, tx))
    cnt = 0
    for y in range(1, N + 1):
        for x in range(1, M + 1):
            if arr[y][x] == 0:
                cnt += 1
    return cnt


N, M = map(int, sys.stdin.readline().split())
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
que = []
zeros = []
mx = 0

maz = [[1] * (M + 2)]
for _ in range(N):
    maz.append([1] + list(map(int, list(sys.stdin.readline().split()))) + [1])
maz.append([1] * (M + 2))

# 바이러스 좌표 데크에 삽입
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if maz[i][j] == 0:
            zeros.append((i, j))
        elif maz[i][j] == 2:
            que.append((i, j))
            # 시험용 미로

for a in zeros:
    zeros.remove(a)
    for b in zeros:
        for c in zeros:
            a1, a2 = a
            b1, b2 = b
            c1, c2 = c

            test = [item[:] for item in maz]
            testq = deque(que[:])
            test[a1][a2] = 1
            test[b1][b2] = 1
            test[c1][c2] = 1
            if mx < bfs(test,testq):
                mx = bfs(test,testq)
print(mx)
