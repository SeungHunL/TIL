import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
que = deque()
que.append((0, N))
used = [0] * 100001
# 최대 길이 만큼 할당
used[N] = 1

while que:
    t, x = que.popleft()
    if x == K:
        print(t)
        break
    t += 1
    # used 중복제거 및 횟수 카운팅
    if x <= 50000 and used[2 * x] == 0:
        used[2 * x] = 1
        que.append((t, 2 * x))
    if x < 100000 and used[x + 1] == 0:
        used[x + 1] = 1
        que.append((t, x + 1))
    if x > 0 and used[x - 1] == 0:
        used[x - 1] = 1
        que.append((t, x - 1))
