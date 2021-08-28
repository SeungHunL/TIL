import sys

stack = []
mx, my = 0, 0
nx, ny = 100000, 100000
count = 0
for _ in range(int(sys.stdin.readline())):
    x, y = map(int, sys.stdin.readline().split())
    stack.append([x, y])
    if mx < x + 10:
        mx = x + 10
    if my < y + 10:
        my = y + 10
    if nx > x:
        nx = x
    if ny > y:
        ny = y
map = [[0] * (mx - nx) for __ in range(my - ny)]
for i in stack:
    for j in range(i[1] - ny, i[1] - ny + 10):
        for k in range(i[0] - nx, i[0] - nx + 10):
            map[j][k] = 1
for n in range(my - ny):
    for m in range(mx - nx):
        if map[n][m]:
            count += 1
print(count)