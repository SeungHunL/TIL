import sys


def gearmove(n, d):
    if d == -1:
        Gears[n] = Gears[n][1:] + Gears[n][0]
    else:
        Gears[n] = Gears[n][-1] + Gears[n][:-1]

def gear_right(n, d):
    while n < 3:
        if Gears[n][2] == Gears[n + 1][-2]:
            break
        else:
            arr.append(((n+1),d*(-1)))
            n += 1
            d *= -1


def gear_left(n, d):
    while n > 0:
        if Gears[n][-2] == Gears[n - 1][2]:
            break
        else:
            arr.append(((n-1),d*(-1)))
            n -= 1
            d *= -1


input = sys.stdin.readline
Gears = []
for i in range(4):
    Gears.append(input().strip())

for i in range(int(input())):
    number, direction = map(int, input().split())
    number -= 1
    arr=[(number,direction)]
    if number == 0:
        gear_right(number, direction)
    elif number == 1:
        gear_right(number, direction)
        gear_left(number, direction)
    elif number == 2:
        gear_right(number, direction)
        gear_left(number, direction)
    else:
        gear_left(number, direction)

    while arr:
        ni,di=arr.pop()
        gearmove(ni, di)
ans = 0
for i in range(len(Gears)):
    if Gears[i][0] == '1':
        ans += 2 ** i
print(ans)
