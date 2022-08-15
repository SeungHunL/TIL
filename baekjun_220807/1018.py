import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for i in range(N):
    board.append(input().strip())
count = [[0] * M for i in range(N)]
ans = 10000
# 1 W
for i in range(N):
    for j in range(M):
        if (i + j) % 2 == 0:
            if board[i][j] == 'B':
                count[i][j] = 1
        else:
            if board[i][j] == 'W':
                count[i][j] = 1

for i in range(N - 7):

    for j in range(M - 7):
        tmp = 0
        for k in range(8):
            tmp += count[i + k][j:j + 8].count(1)
        ans = min(ans, tmp, 64 - tmp)
print(ans)
