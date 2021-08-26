def bfs(x, y, map):
    queue = [(x, y)]
    map[y][x] = 1
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    distance = [[0] * N for ___ in range(N)]
    while queue:
        tx, ty = queue.pop(0)
        map[ty][tx] = 1
        for i in range(4):
            nx = tx + d[i][0]
            ny = ty + d[i][1]
            if map[ny][nx] == 0:
                distance[ny - 1][nx - 1] = distance[ty - 1][tx - 1] + 1
                queue.append((nx, ny))
            elif map[ny][nx] == 2:
                return distance[ty - 1][tx - 1]
    if not queue:
        return 0


for _ in range(int(input())):
    N = int(input())
    Maps = []
    Maps.append([1] * (N + 2))
    for __ in range(N):
        Maps.append([1] + list(map(int, list(input()))) + [1])
    Maps.append([1] * (N + 2))

    for i in range(N + 2):
        for j in range(N + 2):
            if Maps[i][j] == 3:
                sx, sy = j, i
                break

    print(f'#{_ + 1} {bfs(sx, sy, Maps)}')
