import sys

maps = []
for _ in range(5):
    maps.append(list(map(int, sys.stdin.readline().split())))
play = []
for i in range(5):
    play += list(map(int, sys.stdin.readline().split()))

for k in range(len(play)):
    flag = 0
    for y in range(5):
        for x in range(5):
            if maps[y][x] == play[k]:
                maps[y][x] = 0
                flag = 1
                break
        if flag:
            flag = 0
            break

    if k>4:
        d1 = d2 = 0
        for q in range(5):
            sx = sy = 0
            for w in range(5):
                sx += maps[q][w]
                sy += maps[w][q]
            if sx == 0:
                flag += 1
            if sy == 0:
                flag += 1
            d1 += maps[q][q]
            d2 += maps[q][4 - q]
        if d1 == 0:
            flag += 1
        if d2 == 0:
            flag += 1
        if flag >= 3:
            print(k + 1)
            break

