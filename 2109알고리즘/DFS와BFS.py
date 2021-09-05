import sys


def dfs(start, arr):
    visited[start - 1] = 1
    print(start, end=' ')
    for i in range(N):
        if visited[i] != 1 and arr[start - 1][i]:
            dfs(i + 1, arr)


def bfs(start, arr):
    queue=[start - 1]
    while queue:
        k = queue.pop(0)
        visited[k] = 1
        print(k+1,end=' ')
        for n in range(N):
            if visited[n] == 0 and arr[k][n] and n not in queue:
                queue.append(n)


N, M, V = map(int, sys.stdin.readline().split())
maps = [[0] * N for i in range(N)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    maps[a - 1][b - 1] = 1
    maps[b - 1][a - 1] = 1
visited = [0] * N
dfs(V, maps)
print()
visited = [0] * N
bfs(V, maps)
