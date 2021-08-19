for _ in range(10):
    N, T= map(int,input().split())
    ALL = list(map(int,input().split()))
    count = 0
    adj=[[0]*100 for __ in range(2)]
    # print(adj)
    for i in range(0,T*2,2):
        if adj[0][ALL[i]] == 0:
            adj[0][ALL[i]] = ALL[i+1]
        elif adj[1][ALL[i]] == 0:
            adj[1][ALL[i]] = ALL[i+1]
    # 인접행렬
    print(adj[0])
    print(adj[1])
    a = 0
    stack = []
    visited = [0] * 100

    # while 1:
    for p in range(10):
        visited[a] = 1
        if (adj[0][a] != 0) and (visited[adj[0][a]] == 0):
            stack.append(a)
            a = adj[0][a]
        elif (adj[1][a] != 0) and (visited[a] ==1):
            stack.append(a)
            a = adj[1][a]
        while(adj[0][a]):
            visited[adj[0][a]] =1
            stack.append(adj[0][a])
            a = adj[0][a]

    else:

        a = stack.pop()
