def B(G,v,n):
    visited=[0]*n
    queue=[]
    queue.append(v)
    while queue:
        t=queue.pop()
        if not visited[t]:
            visited[t]=1
        for i in G[t]:
            if not visited[i]:
                queue.append(i)
N=7
G=[0]*N
F_I=list(map(int,input().split()))
for i in range(len(list)//2):
    G[F_I[i]].append()
