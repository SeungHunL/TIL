def dijk(start):
    dis = [100000] * (N + 1)
    U = [0] * (N + 1)
    cnt = N
    U[start] = 1
    for i in range(N + 1):
        if adj[start][i]:
            dis[i] = adj[start][i]
    while cnt:
        cnt -= 1
        mn = 100000
        for i in range(N + 1):
            if not U[i]:
                if dis[i] <= mn:
                    idx = i
                    mn = dis[i]
        U[idx] = 1
        for i in range(N + 1):
            if adj[idx][i]:
                dis[i] = min(dis[i], dis[idx] + adj[idx][i])
    if start==X:
        for i in range(1,N+1):
            numl[i]+=dis[i]
    else:
        numl[start]+=dis[X]


for q in range(int(input())):
    N, M, X = map(int, input().split())
    adj = [[0] * (N + 1) for e in range(N + 1)]
    for e in range(M):
        x, y, c = map(int, input().split())
        adj[x][y] = c
    numl = [0]*(N+1)
    for i in range(1, N + 1):
        dijk(i)
    print(f'#{q + 1} {max(numl)}')
