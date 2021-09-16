import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [[] * (N + 1) for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [False] * (N + 1)
visit[1] = True
ans = [0] * (N + 1)
que = deque()

for i in graph[1]:
    ans[i] = 1
    visit[i] = True
    que.append(i)
while que:
    t = que.popleft()
    visit[t] = True
    for j in graph[t]:
        if not visit[j]:
            if not ans[j]:
                ans[j]=t
            que.append(j)
for k in range(2, N + 1):
    print(ans[k])
