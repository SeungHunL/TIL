def dfs(s, c=0):
    global ans
    c += 1
    if c > ans:
        ans = c
    for i in adj[s]:
        if not visit[i]:
            visit[i] = 1
            dfs(i, c)
            visit[i] = 0


for q in range(int(input())):
    N, M = map(int, input().split())
    adj = [[] * (N + 1) for w in range(N + 1)]
    for e in range(M):
        x, y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)
    ans = 1
    for i in range(N):
        visit = [0] * (N + 1)
        visit[i] = 1
        dfs(i)
    print(f'#{q + 1} {ans}')
