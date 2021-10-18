def dijkstra(start,adj,distance):
    U=[start]
    cnt=N
    for i in range(N):
        if adj[start][i]:
            distance[i]=adj[start][i]

    while cnt:
        cnt-=1
        mn=54321
        for j in range(N):
            if j not in U and mn > adj[j]:
                idx=j
                mn=adj[j]
        for k in adj[idx]
N=10
