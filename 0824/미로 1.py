maze = []
for _ in range(10):
    N=int(input())
    for __ in range(16):
        maze.append(input())
    x, y = 1, 1
    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
    hubo = []
    visit = []

    while 1:
        visit.append([y, x])
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if maze[ty][tx] == '0' and [ty,tx] not in visit:
                print(ty,tx,maze[ty][tx])
                hubo.append((ty, tx))
            elif maze[ty][ty] == '3':
                hubo.append((ty, tx))
                break
        print(y,x,hubo)
        if maze[y][x] == '3':
            print(f'#{_ + 1} 1')
            break
        elif not hubo:
            print(f'#{_ + 1} 0')
            break
        y, x = hubo.pop()

