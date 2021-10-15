from collections import deque


def bfs(start):
    que = deque()
    que.append(start)
    while que:
        a = que.popleft()
        vis[a]=1
        for i in tist[a]:
            if not vis[i] and i not in que:
                que.append(i)


for q in range(int(input())):
    N, M = map(int, input().split())
    tist = [[] for m in range(N + 1)]
    for e in range(M):
        a, b = map(int, input().split())
        tist[a].append(b)
        tist[b].append(a)
    vis = [0] * (N + 1)
    ans = 0
    for i in range(1, N + 1):
        if not vis[i]:
            bfs(i)
            ans += 1
    print(f'#{q + 1} {ans}')
