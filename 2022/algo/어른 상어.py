import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
shark_pos = [[0, 0, 0] for _ in range(M + 1)]
maps = [[[0, 0]] * N for _ in range(N)]
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j]:
            shark_pos[line[j]] = [i, j, 0]
            maps[i][j] = [line[j], K]

d_pos = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]

shark_dir = list(map(int, input().split()))
for i in range(M):
    shark_pos[i + 1][2] = shark_dir[i]

shark = [[]]
for i in range(M):
    move = []
    for j in range(4):
        move.append(list(map(int, input().split())))
    shark.append(move)
count = M - 1
time = 0
while count:

    for i in range(1, M + 1):
        y, x, d = shark_pos[i]
        dc = shark[i][d - 1]
        for j in dc:
            dy, dx = d_pos[j]
            ty, tx = y + dy, x + dx
            if 0 <= ty < N and 0 <= tx < N and maps[ty][tx][0] == 0:
                shark_pos[i] = [ty, tx, j]
                break
        else:
            for j in dc:
                dy, dx = d_pos[j]
                ty, tx = y + dy, x + dx
                if 0 <= ty < N and 0 <= tx < N and maps[ty][tx][0] == i:
                    shark_pos[i] = [ty, tx, j]
                    break
    for i in range(N):
        for j in range(N):
            if maps[i][j][0]:
                if maps[i][j][1] == 1:
                    maps[i][j] = [0, 0]
                else:
                    maps[i][j][1] -= 1
    for i in range(1, M + 1):
        y, x, d = shark_pos[i]
        if y >= 0:
            sn, t = maps[y][x]
            if t == K:
                shark_pos[i] = [-1, -1, -1]
                count -= 1
            else:
                maps[y][x] = [i, K]
    time += 1
    if time>1000:
        time=-1
        break
print(time)
