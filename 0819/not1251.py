def dfs(adj, v):
    visited = []
    stack = [v]

    while stack:
        node = stack.pop()
        if node not in visited:

            visited.append(node)
            if node in adj:
                stack.extend(adj[node])
            else:
                pass
    return 0

for _ in range(int(input())):
    N=int(input())
    cp=[]
    L=[]
    for n in range(N):
        cp[n] = list(map(int,input().split()))
    #cp[n] <- (x,y)
    E = float(input())

    while 1:
        for i in range(N):
            for j in range(i,N):

                L += ((cp[i][0]-cp[j][0])**2 + (cp[i][1]-cp[j][1])**2)
                s
    ans = E*(L**2)
    print(f'#{_+1} {ans}')