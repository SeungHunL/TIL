def dfs(adj, st, ed):
    visited = []
    stack = [st]

    while stack:
        node = stack.pop()
        if node == ed:
            return 1
        elif node not in visited:

            visited.append(node)
            if node in adj:
                stack.extend(adj[node])
            else:
                pass
    return 0


for _ in range(int(input())):
    V, E = map(int, input().split())
    ad = {}
    for i in range(E):
        x, y = map(int, input().split())
        if x not in ad:
            ad[x] = [y]
        else:
            ad[x].append(y)
    a, b = map(int, input().split())
    print(f'#{_ + 1} {dfs(ad, a, b)}')
