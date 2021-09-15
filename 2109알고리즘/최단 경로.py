import sys


def dijkstra(start):
    distance[start] = 0
    visit[start] = True
    for k in graph[start]:
        distance[k[0]] = k[1]
    for l in range(V - 1):
        now = get_small_node()
        visit[now] = True
        for m in graph[now]:
            cost = distance[now] + m[1]
            if cost < distance[m[0]]:
                distance[m[0]] = cost


def get_small_node():
    node_min = INF
    index = 0
    for i in range(1, V + 1):
        if not visit[i] and node_min > distance[i]:
            node_min = distance[i]
            index = i
    return index


V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
INF = int(1e9)
graph = [[] for _ in range(V + 1)]
visit = [False] * (V + 1)
distance = [INF] * (V + 1)

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u][v] = w


dijkstra(K)

for l in range(1, V + 1):
    if distance[l] == INF:
        print('INF')
    else:
        print(distance[l])
