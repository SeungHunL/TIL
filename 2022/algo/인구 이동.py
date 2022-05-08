import sys
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

c=0
while 1:
    num = 0
    check = [[0] * N for _ in range(N)]
    flag=False
    pops=[0]
    for i in range(N):
        for j in range(N):
            if check[i][j]:
                pass
            else:
                flag=True
                num += 1
                pop=[maps[i][j]]
                check[i][j] = num
                que = deque()
                que.append((i, j))
                while que:
                    y, x = que.pop()
                    for dy, dx in d:
                        ty, tx = y + dy, x + dx
                        if 0 <= ty < N and 0 <= tx < N and not check[ty][tx] and L <= abs(maps[ty][tx] - maps[y][x]) <= R:
                            check[ty][tx] = num
                            pop.append(maps[ty][tx])
                            que.append((ty, tx))
                pops.append(sum(pop)//len(pop))
    for i in range(N):
        for j in range(N):
            maps[i][j]=pops[check[i][j]]
    if num == N**2:
        break
    c+=1

print(c)
