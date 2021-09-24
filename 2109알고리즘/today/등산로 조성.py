dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def dfs(graph, start, visit=[], flag=1):
    global mx
    visit.append(start)
    if mx < len(visit):
        mx = len(visit)
    ty, tx = start
    for i in range(4):
        ry = ty + dy[i]
        rx = tx + dx[i]
        if 0 <= ry < N and 0 <= rx < N:
            if graph[ty][tx] > graph[ry][rx]:
                if (ry, rx) not in visit:
                    dfs(graph, (ry, rx), visit, flag)
            if flag and graph[ry][rx] >= graph[ty][tx] > graph[ry][rx] - K:
                a = graph[ry][rx]
                flag = 0
                graph[ry][rx] = graph[ty][tx] - 1
                if (ry, rx) not in visit:
                    dfs(graph, (ry, rx), visit, flag)
                flag = 1
                graph[ry][rx] = a
    visit.pop()


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    maps = []
    for __ in range(N):
        maps.append(list(map(int, input().split())))

    # 봉우리 찾기
    high = 0
    top = []
    for i in range(N):
        for j in range(N):
            if maps[i][j] == high:
                top.append((i, j))
            elif maps[i][j] > high:
                high = maps[i][j]
                top = [(i, j)]
    # 등산로
    mx = 0
    for k in top:
        dfs(maps, k)
    print(f'#{_ + 1} {mx}')
