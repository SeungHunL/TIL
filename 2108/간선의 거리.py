def bfs(G, start, end, N):
    distance = [0] * N
    visited = [0] * N
    visited[start] = 1
    queue = [start]
    while queue:
        t = queue.pop(0)
        if not visited[t]:
            visited[t] = 1

        for i in G[t]:
            if not visited[i]:
                queue.append(i)
                if not distance[i]:
                    distance[i] = distance[t] + 1
                if i == end:
                    return distance[i]
    return 0


for _ in range(int(input())):
    V, E = map(int, input().split())
    node = [[] for __ in range(V + 1)]
    for __ in range(E):
        s, e = map(int, input().split())
        node[s].append(e)
        node[e].append(s)

    s, g = map(int, input().split())  # 1,6
    print(f'#{_ + 1} {bfs(node, s, g, V + 1)}')
