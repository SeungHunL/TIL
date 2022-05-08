import sys


def tornado():
    t = 1
    y, x = N // 2 + 2, N // 2 + 2
    direction = 1
    while 1:
        for j in range(t):
            if (y, x) == (2, 2):
                return
            if direction == 1:
                x -= 1
                amount = maps[y][x]
                a = maps[y][x]
                a -= (int(amount * 0.07) + int(amount * 0.07) + int(amount * 0.02) + int(amount * 0.02) + int(
                    amount * 0.01) + int(amount * 0.01) + int(amount * 0.1) + int(amount * 0.1) + int(amount * 0.05))
                maps[y][x] = 0
                maps[y][x - 1] += a
                maps[y - 1][x] += int(amount * 0.07)
                maps[y + 1][x] += int(amount * 0.07)
                maps[y - 1][x - 1] += int(amount * 0.1)
                maps[y + 1][x - 1] += int(amount * 0.1)
                maps[y - 1][x + 1] += int(amount * 0.01)
                maps[y + 1][x + 1] += int(amount * 0.01)
                maps[y - 2][x] += int(amount * 0.02)
                maps[y + 2][x] += int(amount * 0.02)
                maps[y][x - 2] += int(amount * 0.05)
            elif direction == 2:
                y += 1
                amount = maps[y][x]
                a = maps[y][x]
                a -= (int(amount * 0.07) + int(amount * 0.07) + int(amount * 0.02) + int(amount * 0.02) + int(
                    amount * 0.01) + int(amount * 0.01) + int(amount * 0.1) + int(amount * 0.1) + int(amount * 0.05))
                maps[y][x] = 0
                maps[y+1][x] += a
                maps[y ][x+1] += int(amount * 0.07)
                maps[y ][x-1] += int(amount * 0.07)
                maps[y - 1][x - 1] += int(amount * 0.01)
                maps[y + 1][x - 1] += int(amount * 0.1)
                maps[y - 1][x + 1] += int(amount * 0.01)
                maps[y + 1][x + 1] += int(amount * 0.1)
                maps[y][x+2] += int(amount * 0.02)
                maps[y][x-2] += int(amount * 0.02)
                maps[y+2][x] += int(amount * 0.05)
            elif direction == 3:
                x += 1
                amount = maps[y][x]
                a = maps[y][x]
                a -= (int(amount * 0.07) + int(amount * 0.07) + int(amount * 0.02) + int(amount * 0.02) + int(
                    amount * 0.01) + int(amount * 0.01) + int(amount * 0.1) + int(amount * 0.1) + int(amount * 0.05))
                maps[y][x] = 0
                maps[y][x + 1] += a
                maps[y - 1][x] += int(amount * 0.07)
                maps[y + 1][x] += int(amount * 0.07)
                maps[y - 1][x - 1] += int(amount * 0.01)
                maps[y + 1][x - 1] += int(amount * 0.01)
                maps[y - 1][x + 1] += int(amount * 0.1)
                maps[y + 1][x + 1] += int(amount * 0.1)
                maps[y - 2][x] += int(amount * 0.02)
                maps[y + 2][x] += int(amount * 0.02)
                maps[y][x + 2] += int(amount * 0.05)
            else:
                y -= 1
                amount = maps[y][x]
                a = maps[y][x]
                a -= (int(amount * 0.07) + int(amount * 0.07) + int(amount * 0.02) + int(amount * 0.02) + int(
                    amount * 0.01) + int(amount * 0.01) + int(amount * 0.1) + int(amount * 0.1) + int(amount * 0.05))
                maps[y][x] = 0
                maps[y - 1][x] += a
                maps[y][x + 1] += int(amount * 0.07)
                maps[y][x - 1] += int(amount * 0.07)
                maps[y - 1][x - 1] += int(amount * 0.1)
                maps[y + 1][x - 1] += int(amount * 0.01)
                maps[y - 1][x + 1] += int(amount * 0.1)
                maps[y + 1][x + 1] += int(amount * 0.01)
                maps[y][x + 2] += int(amount * 0.02)
                maps[y][x - 2] += int(amount * 0.02)
                maps[y - 2][x] += int(amount * 0.05)
        direction += 1
        direction %= 4
        if direction % 2 == 1:
            t += 1


input = sys.stdin.readline
N = int(input())
maps = [[0] * (N + 4),[0] * (N + 4)]
for _ in range(N):
    maps.append([0] * 2 + list(map(int, input().split())) + [0] * 2)
maps.append([0] * (N + 4))
maps.append([0] * (N + 4))


before = 0
for _ in maps:
    before += sum(_)
tornado()
after = 0
for _ in range(2, len(maps) - 2):
    after += sum(maps[_][2:-2])
print(before - after)

# print(list(map(list,zip(maps))))
# def rotate(_arr):
#     return list(map(list, zip(*_arr)))[::-1]
# for i in rotate(maps):
#     print(i)