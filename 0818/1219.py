for _ in range(10):
    N, T= map(int,input().split())
    ALL = list(map(int,input().split()))
    count = 0
    adj=[[0]*2 for __ in range(100)]
    print(adj)
    for i in range(100):
        if adj[ALL[i]][ALL[i+1]] == 0:
            adj[ALL[i]][ALL[i+1]] = 1
        elif adj[ALL[i]][ALL[i+1]] == 1:
            adj[ALL[i]][ALL[i + 1]] = 1
