import sys

A, B, x, y, p, q = map(int, sys.stdin.readline().split())
points = [(0, 0), (A, 0), (0, B), (A, B)]
cnt = 0
wall = {}
while 1:
    if (x, y) in points:
        print(cnt)
        break

    a = ((A - x) / p) if p > 0 else (x / -p)
    b = ((B - y) / q) if q > 0 else (y / -q)
    if a >= b:
        if q > 0:
            x, y = x + b * p, B
        else:
            x, y = x + b * p, 0
        q *= -1
    else:
        if p > 0:
            x, y = A, y + a * q
        else:
            x, y = 0, y + a * q
        p *= -1
    cnt += 1
    if (x, y) in wall:
        wall[(x, y)] += 1
        if wall[(x, y)] == 4:
            print(-1)
            break
    else:
        wall[(x, y)] = 1
