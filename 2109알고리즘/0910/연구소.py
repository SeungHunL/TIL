import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
# 데크
que = deque()
# 벽
maz = [[1] * (M + 2)]
print(maz)
for _ in range(N):
    maz.append([1] + list(map(int, list(sys.stdin.readline().split()))) + [1])
maz.append([1] * (M + 2))
# 델타
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
# 바이러스 좌표 데크에 삽입
stack = []
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if maz[i][j] == 2:
            used = [0, 0, 0]
            cnt = 0
            que.append((i, j))
            # 벽 0,1,2개로 막아질 때 갯수 카운트
            while que:
                y, x = que.popleft()
                cnt += 1
                for k in range(4):
                    tx, ty = x + dx[k], y + dy[k]
                    if not maz[ty][tx]:
                        maz[ty][tx] = 3
                        que.append((ty, tx))
                #
                if used==[0,1,1]:
                    break
                elif len(que) == 1 and not used[1]:
                    used[1] = cnt
                elif len(que) == 2 and not used[2]:
                    used[2] = cnt

            stack.append(used)
print(stack)
