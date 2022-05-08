import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
maps = [[5] * N for _ in range(N)]
A = []
trees = [[[]for _ in range(N)] for __ in range(N)]
rc = [(-1, 0), (-1, -1), (-1, 1), (1, 0), (1, -1), (1, 1), (0, -1), (0, 1)]
for n in range(N):
    A.append(list(map(int, input().split())))
for m in range(M):
    y, x, c = map(int, input().split())
    trees[y - 1][x - 1].append(c)
# 봄 / 여름
for k in range(K):
    for y in range(N):
        for x in range(N):
            if trees[y][x]:
                trees[y][x].sort()
                for i in range(len(trees[y][x])):
                    if trees[y][x][i]<=maps[y][x]:
                        maps[y][x]-=trees[y][x][i]
                        trees[y][x][i]+=1
                    else:
                        for j in range(i,len(trees[y][x])):
                            maps[y][x]+=int(trees[y][x][j]/2)
                        trees[y][x]=trees[y][x][:i]
                        break
    # 가을
    for y in range(N):
        for x in range(N):
            if trees[y][x]:
                for i in range(len(trees[y][x])):
                    if trees[y][x][i] % 5==0:  # 나이가 5의 배수일 때/ 번식
                        for r, c in rc:
                            tx, ty = c + x, r + y
                            if 0 <= tx < N and 0 <= ty < N:
                                trees[ty][tx].append(1)
    # 겨울
    for r in range(N):
        for c in range(N):
            maps[r][c] += A[r][c]
ans = 0
for y in range(N):
    for x in range(N):
        ans += len(trees[y][x])
print(ans)
