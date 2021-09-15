import sys
import heapq


V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
INF = int(1e9)
graph = [[] for _ in range(V + 1)]
distance = [INF] * (V + 1)

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for k in graph[now]:
            cost = dist + k[1]
            if cost < distance[k[0]]:
                distance[k[0]] = cost
                heapq.heappush(q,(cost,k[0]))


dijkstra(K)

for l in range(1, V + 1):
    if distance[l] == INF:
        print('INF')
    else:
        print(distance[l])