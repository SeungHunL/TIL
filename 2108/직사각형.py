import sys

for _ in range(4):
    sq = list(map(int, sys.stdin.readline().split()))
    cx = cy = 0
    for i in range(sq[0], sq[2] + 1):
        if sq[4] <= i <= sq[6]:
            cx += 1
    for j in range(sq[1], sq[3] + 1):
        if sq[5] <= j <= sq[7]:
            cy += 1
    if cx > 1 and cy > 1:
        print('a')
    elif (cx == 1 and cy > 1) or (cy == 1 and cx > 1):
        print('b')
    elif cx == 1 and cy == 1:
        print('c')
    else:
        print('d')
