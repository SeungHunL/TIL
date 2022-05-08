import sys
from collections import deque

input = sys.stdin.readline


def snakemove():
    time = 1
    snake = deque([(0, 0)])
    direction = 1
    for X, C in moves:
        hy, hx = snake[-1]
        while time <= X:
            if direction == 1:
                hx += 1
            elif direction == 2:
                hy += 1
            elif direction == 3:
                hx -= 1
            else:
                hy -= 1
            if 0 <= hx < N and 0 <= hy < N:
                if (hy, hx) in snake:
                    print(time)  # 뱀의 몸에 부딪혔을 때
                    return
                snake.append((hy, hx))
                if maps[hy][hx]:
                    maps[hy][hx] = 0
                else:
                    snake.popleft()
                time += 1
            else:
                print(time)
                return
        if C == 'L':
            direction -= 1
            direction %= 4
        else:
            direction += 1
            direction %= 4
    hy, hx = snake[-1]
    while 1:
        if direction == 1:
            hx += 1
        elif direction == 2:
            hy += 1
        elif direction == 3:
            hx -= 1
        else:
            hy -= 1
        if 0 <= hx < N and 0 <= hy < N:
            if (hy, hx) in snake:
                print(time)  # 뱀의 몸에 부딪혔을 때
                return
            snake.append((hy, hx))
            if maps[hy][hx]:
                maps[hy][hx] = 0
            else:
                snake.popleft()
            time += 1
        else:
            print(time)  # 지도 밖으로 나갔을 때
            return


N = int(input())
maps = [[0] * N for _ in range(N)]
for _ in range(int(input())):
    y, x = map(int, input().split())
    maps[y - 1][x - 1] = 1
moves = []
for _ in range(int(input())):
    X, C = input().split()
    moves.append((int(X), C))
snakemove()
