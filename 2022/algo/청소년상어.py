import sys

input = sys.stdin.readline


def fish_move(smap, fishlist):
    for i in range(1, 17):
        c, y, x, direction = fishlist[i]
        if not c:  # 잡히지 않았을 때
            for j in range(8):
                dy, dx = d[(direction + j) % 8]
                ty, tx = y + dy, x + dx
                if 0 <= ty < 4 and 0 <= tx < 4 and smap[ty][tx] != -1:
                    fishlist[i] = [False, ty, tx, (direction + j) % 8]
                    fishlist[smap[ty][tx]][1] = y
                    fishlist[smap[ty][tx]][2] = x
                    smap[ty][tx], smap[y][x] = smap[y][x], smap[ty][tx]
                    break
    return smap, fishlist


def shark_move(smap, fishlist):
    global t, shark
    if t == 1:
        eaten = smap[0][0]
        fishlist[eaten][0] = True
        shark = [0, 0, fishlist[eaten][3]]
        smap[0][0] = -1
    else:
        t += 1
        y, x, direction = shark
        dy, dx = d[direction]
        for i in range(1, 3):
            ty, tx = y + dy * i, x + dx * i
            if 0 <= ty < 4 and 0 <= tx < 4 and smap[ty][tx] > 0:
                eaten = smap[ty][tx]
                fishlist[eaten][0] = True
                shark = [ty, tx, fishlist[eaten][3]]
                smap[ty][tx] = -1
                shark_move(fish_move(smap, fishlist))
        else:
            t -= 1
            return


# 7 6 2 3 15 6 9 8
# 3 1 1 8 14 7 10 1
# 6 1 13 6 4 3 11 4
# 16 1 8 7 5 2 12 2
maps = [[0] * 4 for __ in range(4)]
fishes = [[False, 0, 0]] * 17
for _ in range(4):
    line = list(map(int, input().split()))
    for __ in range(4):
        maps[_][__] = line[2 * __]
        fishes[line[2 * __]] = [False, _, __, line[2 * __ + 1] - 1]
d = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), ]
max_score = 0

shark_move(maps, fishes)
print(max_score)
