import sys
import copy

input = sys.stdin.readline


def fish_move(board,sha):
    for a in range(1, 17):
        y = x = -1
        for b in range(4):
            for k in range(4):
                if board[b][k][0] == a:
                    y, x = b, k
                    break
        if y == -1 and x == -1:
            continue
        direction = board[y][x][1]
        for l in range(8):
            dy, dx = d[(direction + l) % 8]
            ty, tx = y + dy, x + dx
            if 0 <= ty < 4 and 0 <= tx < 4 and not (ty == sha[0] and tx == sha[1]):
                board[y][x][1] = (direction + l) % 8
                board[ty][tx], board[y][x] = board[y][x], board[ty][tx]
                break
    return board


def shark_move(smap, score, sh):
    global max_score
    sy, sx = sh
    score += smap[sy][sx][0]
    max_score = max(max_score, score)
    smap[sy][sx][0] = 0
    direction = smap[sy][sx][1]
    nmap = fish_move(smap,sh)
    dy, dx = d[direction]
    for q in range(1, 4):
        ty, tx = sy + dy * q, sx + dx * q
        if 0 <= ty < 4 and 0 <= tx < 4 and nmap[ty][tx][0] > 0:
            shark_move(copy.deepcopy(nmap), score, [ty, tx])


maps = [[[0, 0]] * 4 for __ in range(4)]
for i in range(4):
    line = list(map(int, input().split()))
    for j in range(4):
        maps[i][j] = [line[2 * j], line[2 * j + 1] - 1]
d = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
max_score = 0
shark = [0, 0]  # 먹은 거, 방향, y, x]
eat = 0
shark_move(maps, eat, shark)
print(max_score)
