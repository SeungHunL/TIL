import sys

input = sys.stdin.readline

N, M = map(int, input().split())
y, x, d = map(int, input().split())
D = [(-1, 0), (0, 1), (1, 0), (0, -1)]
maps = [list(map(int, input().split())) for _ in range(N)]
check = [[0] * M for _ in range(N)]
while 1:
    # 1
    check[y][x]=1
    # 2
    for _ in range(4):
        d = (d + 3) % 4  # 방향 전환
        dy, dx = D[d]
        ty, tx = y + dy, x + dx
        if maps[ty][tx] == 0 and check[ty][tx] == 0:  # 빈 공간일 때
            y, x = ty, tx
            break
    else:
        if maps[y - dy][x - dx]:
            break
        else:
            y -= dy
            x -= dx
print(sum(list(map(sum,check))))
