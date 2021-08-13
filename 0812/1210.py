# 입력
for num in range(10):
    N = int(input())
    lad = [0] * 100
    for n in range(100):
        lad[n] = list(map(int, input().split()))

    # 빈 2차원 리스트 생성
    for x in range(100):
        ans = x
        y = 0
        r = l = b = 0

        if lad[y][x] == 1:
            for i in range(300):
                print(x, y)

                if (lad[y][x] == 2) or (y == 99):
                    break

                elif x != 99 and (lad[y][x + 1] == 1) and (l == 0):
                    x += 1
                    r = 1
                    b = l = 0
                elif x != 0 and (lad[y][x - 1] == 1) and (r == 0):
                    x -= 1
                    l = 1
                    b = r = 0
                elif lad[y + 1][x] == 1:
                    y += 1
                    b = 1
                    l = r = 0

                else:
                    break

        if lad[99][x] == 2:
            print(f'#{num + 1} {ans}')
            break
