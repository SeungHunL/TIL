import sys

input = sys.stdin.readline
N, M, y, x, K = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(N)]
dice = [0] * 6
d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
h = [0] * 5
v = [0] * 5
for command in list(map(int, input().split())):

    dy, dx = d[command - 1]
    ty, tx = dy + y, dx + x
    if 0 <= ty < N and 0 <= tx < M:

        if command == 4:
            v = v[1:] + [v[-1]]
            h[0] = h[-1] = v[-1] = v[0]
            h[2] = v[2]
        elif command == 3:
            v = [v[-1]] + v[:-1]
            h[0] = h[-1] = v[0] = v[-1]
            h[2] = v[2]
        elif command == 2:
            h = [h[-1]] + h[:-1]
            v[0] = v[-1] = h[0] = h[-1]
            v[2] = h[2]
        else:
            h = h[1:] + [h[-1]]
            v[0] = v[-1] = h[-1] = h[0]
            v[2] = h[2]
        # print(ty,tx,maps[ty][tx])
        # print(maps)
        if maps[ty][tx]:
            h[2] = v[2] = maps[ty][tx]
            maps[ty][tx] = 0
        else:
            maps[ty][tx] = h[2]

        y, x = ty, tx
        print(v[0])
