def shot(start, count=0):
    if count > 3:
        return
    y, x = start
    if y < N - 2:
        c = 0
        for i in range(y + 1, N):
            if maps[i][x]:
                if c == 1 and count<3: # 먹을 돌이 있을 때
                    res[i][x] = 1
                    maps[i][x]=0
                    shot((i, x), count + 1)
                    maps[i][x]=1
                    break
            if c == 1 and count < 3: # 먹을 돌이 없을 때
                shot((i, x), count + 1)
            if maps[i][x]:
                c+=1

    if 1 < y:
        c = 0
        for j in range(y - 1, -1, -1):
            if maps[j][x]:
                if c == 1 and count < 3:  # 먹을 돌이 있을 때
                    res[j][x] = 1
                    maps[j][x] = 0
                    shot((j, x), count + 1)
                    maps[j][x] = 1
                    break
            if c == 1 and count < 3:  # 먹을 돌이 없을 때
                shot((j, x), count + 1)
            if maps[j][x]:
                c += 1
    if x < N - 2:
        c = 0
        for k in range(x + 1, N):
            if maps[y][k]:
                if c == 1 and count < 3:  # 먹을 돌이 있을 때
                    res[y][k] = 1
                    maps[y][k] = 0
                    shot((y, k), count + 1)
                    maps[y][k] = 1
                    break
            if c == 1 and count < 3:  # 먹을 돌이 없을 때
                shot((y, k), count + 1)
            if maps[y][k]:
                c += 1
    if 1 < x:
        c = 0
        for l in range(x - 1, -1, -1):
            if maps[y][l]:
                if c == 1 and count < 3:  # 먹을 돌이 있을 때
                    res[y][l] = 1
                    maps[y][l] = 0
                    shot((y, l), count + 1)
                    maps[y][l] = 1
                    break
            if c == 1 and count < 3:  # 먹을 돌이 없을 때
                shot((y, l), count + 1)
            if maps[y][l]:
                c += 1


for q in range(int(input())):
    N = int(input())
    maps = []
    for m in range(N):
        maps.append(list(map(int, input().split())))
    flag = 0
    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 2:
                flag = 1
                start = (i, j)
                maps[i][j]=0
                break
        if flag:
            break
    res = [[0] * N for n in range(N)]  # 도달할 수 있는 좌표를 표시할 이차원 리스트
    shot(start)
    ans = 0
    for k in range(N):
        for l in range(N):
            if res[k][l]:
                ans += 1
    print(f'#{q + 1} {ans}')
