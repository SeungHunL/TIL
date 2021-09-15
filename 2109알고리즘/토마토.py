import sys
from collections import deque


def bfs(arr):
    mx = 0
    que = deque()
    zcnt = 0
    for m in range(1, M + 1):
        for n in range(1, N + 1):
            if arr[m][n] == 1:
                # 시작하는 지점 찾기
                que.append((m, n))
                # 0 세기
            elif arr[m][n] == 0:
                zcnt += 1
    while que:
        (ty, tx) = que.popleft()
        # 최댓값 찾기
        if arr[ty][tx] > mx:
            mx = arr[ty][tx]
        for k in range(4):
            ry, rx = ty + dy[k], tx + dx[k]
            if arr[ry][rx] == 0:
                que.append((ry, rx))
                zcnt -= 1
                # 옆에서 먼저 익은 토마토가 익는데 걸린 시간
                arr[ry][rx] = arr[ty][tx] + 1
    if zcnt:
        print(-1)
    else:
        # 0일차에 1인 토마토 초기값:2
        print(mx - 1)
    return


dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
N, M = map(int, sys.stdin.readline().split())

box = [[1] * (N + 2)]
for _ in range(M):
    box.append([1] + list(map(int, sys.stdin.readline().split())) + [1])
box.append([1] * (N + 2))
bfs(box)
