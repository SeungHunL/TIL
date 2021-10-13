from collections import deque


def bfs(start):
    global ans
    res = []
    que = deque()
    que.append(start)
    cnt = 1
    while que:
        s = que.popleft()
        visit[s] = 1
        cnt -= 1
        if s in adj:
            for i in adj[s]:
                if not visit[i]and i not in que:
                    que.append(i)
                    res.append(i)
        if cnt == 0:
            cnt = len(res)
            ans.append(res)
            res = []


for q in range(10):
    N, M = map(int, input().split())
    adj = {}
    tlist = list(map(int, input().split()))
    for e in range(N // 2):
        x = tlist[2 * e]
        y = tlist[2 * e + 1]
        if x not in adj:
            adj[x] = [y]
        else:
            adj[x].append(y)
    ans = []
    visit = [0] * 101
    bfs(M)
    print(ans)
    print(f'#{q + 1} {max(ans[-2])}')
