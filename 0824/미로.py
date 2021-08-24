for _ in range(int(input())):
    maze = []
    N = int(input())

    maze.append('1'*(N+2))
    for __ in range(N):
        maze.append('1'+input()+'1')
    maze.append('1'*(N+2))

    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
    hubo = []
    visit = []

    for x_find in range(N+1):
        for y_find in range(N+1):
            if maze[y_find][x_find] == '2':
                x, y = x_find, y_find
                break
    while 1:
        visit.append([y, x])
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if maze[ty][tx] == '3':
                hubo.append((ty, tx))
                break
            elif maze[ty][tx] == '0' and [ty, tx] not in visit:
                # print(ty, tx, maze[ty][tx])
                hubo.append((ty, tx))

        if maze[ty][tx] == '3':
            print(f'#{_ + 1} 1')
            break
        elif not hubo:
            print(f'#{_ + 1} 0')
            break
        y, x = hubo.pop()
