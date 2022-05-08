import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
maps = [[5] * N for _ in range(N)]
A = []
trees = []
rc = [(-1, 0), (-1, -1), (-1, 1), (1, 0), (1, -1), (1, 1), (0, -1), (0, 1)]
for n in range(N):
    A.append(list(map(int, input().split())))
for m in range(M):
    y, x, c = map(int, input().split())
    trees.append([y - 1, x - 1, c])
for k in range(K):
    trees.sort(key=lambda x: x[2])
    summers = []  # 죽을 나무
    # 봄
    for i in range(len(trees)):
        y, x, c = trees[i]
        if maps[y][x] >= c:  # 양분을 먹을 때
            maps[y][x] -= c
            trees[i][2] += 1
        else:  # 죽을 때
            summers.append([i, y, x, c / 2])  # 죽을 나무 추가
    # 여름
    for s in summers[::-1]: # 리스트를 앞에서 부터 삭제하면 꼬임
        i, y, x, c = s
        del trees[i]
        maps[y][x] += int(c)
    # 가을
    for i in range(len(trees)):
        y, x, c = trees[i]
        if c % 5:  # 나이가 5의 배수가 아닐 때
            pass
        else:  # 번식
            for r, c in rc:
                tx, ty = c + x, r + y
                if 0 <= tx < N and 0 <= ty < N:
                    trees.append([ty, tx, 1])
    # 겨울
    for r in range(N):
        for c in range(N):
            maps[r][c] += A[r][c]
print(len(trees))
