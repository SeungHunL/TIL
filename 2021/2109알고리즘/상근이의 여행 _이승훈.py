import sys
from collections import deque

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    visit = [False] * (N + 1)
    graph = [[] for i in range(N + 1)]
    plane = []
    for __ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    que = deque()
    que.append(1)
    cnt = -1
    while que:
        start = que.popleft()
        visit[start] = True
        for i in graph[start]:
            if not visit[i] and i not in que:
                que.append(i)
        cnt += 1
    print(cnt)
