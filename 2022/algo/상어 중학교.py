import sys
from collections import deque

def gravity(board):
    for j in range(N):
        nb = -1
        for i in range(N - 1, -1, -1):
            if board[i][j] == -2 and nb == -1:
                nb = i
            elif board[i][j] >= 0 and nb >= 0:
                board[nb][j] = board[i][j]
                board[i][j] = -2
                nb = i
            elif board[i][j] == -1:
                nb = -1
    return board

def fb(board):
    # for b in board:
    #     print(b)
    global ans
    check = [[0] * N for _ in range(N)]
    max_score = 0
    now = []
    for i in range(N):
        for j in range(N):
            if check[i][j] == 0 and board[i][j] != -1 and board[i][j] != -2:
                block = {(i, j)}
                score = 1
                v = board[i][j]
                check[i][j] = 1
                q = deque([(i, j)])
                while q:
                    y, x = q.popleft()
                    for dy, dx in d:
                        ty, tx = y + dy, x + dx
                        if 0 <= ty < N and 0 <= tx < N:
                            if check[ty][tx] == 0 and (ty, tx) not in block:
                                if board[ty][tx] == v:
                                    score += 1
                                    block.add((ty, tx))
                                    check[ty][tx] = 1
                                    q.append((ty, tx))
                                elif board[ty][tx] == 0:
                                    score += 1
                                    block.add((ty, tx))
                                    q.append((ty, tx))
                if max_score < score:
                    max_score = score
                    now = block
    a = len(now)
    if a>1:
        for y, x in now:
            board[y][x] = -2
        ans += a ** 2
        # print()
        # for b in board:
        #     print(b)
        board = gravity(board)
        board = list(map(list, zip(*board)))[::-1]
        # print()
        # for b in board:
        #     print(b)
        board = gravity(board)
        # print()
        # for b in board:
        #     print(b)
        # print(ans)
        fb(board)
    else:
        print(ans)

    #     fb(board)
    # else:
    #     return


input = sys.stdin.readline

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N, M = map(int, input().split())
maps = []
ans = 0
for _ in range(N):
    maps.append(list(map(int, input().split())))
fb(maps)
