def dik(start):
    U[start]=1
    cnt=0
    for i in range(N+1):
        if adj[start][i]:
            dis[i]=adj[start][i]
    while 1:
        if cnt==N:
            break
        cnt+=1
        mn = 100000
        for i in range(N+1):
            if not U[i]:
                if dis[i]<=mn:
                    idx = i
                    mn=dis[i]
        U[idx]=1
        for i in range(N + 1):
            if adj[idx][i]:
                dis[i]=min(dis[i],dis[idx]+adj[idx][i])

for q in range(int(input())):
    N, E = map(int, input().split())
    adj = [[0] * (N + 1) for a in range(N + 1)]
    for o in range(E):
        s, e, w = map(int, input().split())
        adj[s][e]= w
    dis=[100000]*(N+1)
    U=[0]*(N+1)
    dik(0)
    print(f'#{q + 1} {dis[N]}')
