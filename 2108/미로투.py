def bfs(x, y, map):
    queue = [(x, y)]
    map[y][x] = 1
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while queue:
        tx, ty = queue.pop(0)
        map[ty][tx] = 1
        for i in range(4):
            nx = tx + d[i][0]
            ny = ty + d[i][1]
            print(ny, nx)
            if map[ny][nx] == 0:
                print(ny, nx)
                queue.append((nx, ny))
            elif map[ny][nx] == 3:
                return 1
    if not queue:
        return 0


for _ in range(10):

    T = int(input())
    maze = []
    for __ in range(16):
        maze.append(list(map(int, list(input()))))
    print(maze)
    print(f'#{_ + 1} {bfs(1, 1, maze)}')
