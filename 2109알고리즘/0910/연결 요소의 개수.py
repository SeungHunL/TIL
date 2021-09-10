import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
# 인접리스트
num_list = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    num_list[a].append(b)
    num_list[b].append(a)
# 사용 확인
used = [0] * (N + 1)
# 데크 사용
que = deque()
cnt = 0
for i in range(1, N + 1):
    # 사용 x
    if not used[i]:
        que.append(i)
        # 사용하지않은 원소와 연결된 다른 원소들 전부 사용 처리
        while que:
            x = que.popleft()
            for j in num_list[x]:
                if not used[j]:
                    que.append(j)
                    used[j] = 1
        # 연결 요소 하나 clear
        cnt += 1
print(cnt)
