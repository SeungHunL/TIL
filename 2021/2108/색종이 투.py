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
maps = [[0] * (mx - nx + 2) for __ in range(my - ny + 2)]
for i in stack:
    for j in range(i[1] - ny + 1, i[1] - ny + 11):
        for k in range(i[0] - nx + 1, i[0] - nx + 11):
            maps[j][k] = 1
for n in range(my - ny + 2):
    for m in range(mx - nx + 2):
        if maps[n][m] == 0:
            if m + 1 <= mx - nx + 1 and maps[n][m + 1] == 1:
                count += 1
            if n + 1 <= my - ny + 1 and maps[n + 1][m] == 1:
                count += 1
            if n - 1 >= 0 and maps[n - 1][m] == 1:
                count += 1
            if m - 1 >= 0 and maps[n][m - 1] == 1:
                count += 1
print(count)