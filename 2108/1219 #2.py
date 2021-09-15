def dfs(adj, v):
    visited = []
    stack = [v]

    while stack:
        node = stack.pop()
        if node ==99:
            return 1
        elif node not in visited:

            visited.append(node)
            if node in adj:
                stack.extend(adj[node])
            else:
                pass
    return 0


for _ in range(10):
    N, T = map(int, input().split())
    ALL = list(map(int, input().split()))
    adj = {}
    # print(adj)
    for i in range(0, T * 2, 2):
        if ALL[i] not in adj:
            adj[ALL[i]] = [ALL[i + 1]]
        else:
            adj[ALL[i]].append(ALL[i + 1])

    # 인접행렬
    print(f'#{_+1} {dfs(adj,0)}')