import sys
from collections import deque

input = sys.stdin.readline

d = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
d2 = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
clouds = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]
for _ in range(M):
    check = [[0] * N for _ in range(N)]
    dir, s = map(int, input().split())
    dy, dx = d[dir - 1]
    # 1 모든 구름 이동
    while clouds:
        y, x = clouds.pop()
        y += dy * s
        x += dx * s
        while y < 0:
            y += N
        if y > N - 1:
            y %= N
        while x < 0:
            x += N
        if x > N - 1:
            x %= N
        # 2 구름에서 비
        maps[y][x] += 1
        check[y][x] = 1
    # 3 구름이 모두 사라진다

    for i in range(N):
        for j in range(N):
            if check[i][j]:
                c = 0
                for sy, sx in d2:
                    my, mx = i + sy, j + sx
                    if 0 <= mx < N and 0 <= my < N and maps[my][mx]:
                        c += 1
                maps[i][j] += c
    for i in range(N):
        for j in range(N):
            if maps[i][j] >= 2 and check[i][j] != 1:
                clouds.append((i, j))
                maps[i][j] -= 2
print(sum(list(map(sum, maps))))
