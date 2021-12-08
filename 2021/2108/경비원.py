import sys

w, h = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
tor = []
for _ in range(N):
    tor.append(list(map(int, sys.stdin.readline().split())))
x, y = map(int, sys.stdin.readline().split())
s = 0
for i in tor:
    if i[0] == x:
        s += abs(i[1] - y)
    elif i[0] in (1, 2) and x in (1, 2):
        s += (h + i[1] + y) if i[1] + y < 2 * w - i[1] - y else 2 * w - i[1] - y+h
    elif i[0] in (3, 4) and x in (3, 4):
        s += (w + i[1] + y) if i[1] + y < 2 * h - i[1] - y else 2 * h - i[1] - y+w
    elif (i[0], x) in [(1, 3), (3, 1)]:
        s += y + i[1]
    elif (i[0], x) in [(3, 2), (2, 3)]:
        if i[0] == 3:
            s += y - i[1] + h
        else:
            s += -y + i[1] + h
    elif (i[0], x) in [(2, 4), (4, 2)]:
        s += -y - i[1] + w + h
    elif (i[0], x) in [(4, 1), (1, 4)]:
        if i[0] == 4:
            s += -y + i[1] + w
        else:
            s += y - i[1] + w
print(s)