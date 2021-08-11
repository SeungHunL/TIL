    # 입력
T = int(input())
for num in range(T):
    N = int(input())
    snail = [0]*N
    for m in range(N):
        for n in range(N):
            snail[m]=[0]*N
    # 빈 2차원 리스트 생성
    cnt = 0
    x = y = 0
    for i in range(1 , N*N+1):
        snail[y][x]=i
        print(snail)
        if ((x,y) in ((0,N-1),(N-1,N-1),(N-1,0))) == 1:
            cnt += 1
        if cnt % 4 == 0:
            x += 1
        elif cnt % 4 == 1:
            y += 1
        elif cnt % 4 == 2:
            x -= 1
        elif cnt % 4 == 3:
            y -= 1
        print(x,y)
        if N == 1:
            break
        elif snail[y][x] != 0:
            if cnt % 4 == 0:
                x -= 1
                y += 1
            elif cnt % 4 == 1:
                x -= 1
                y -= 1
            elif cnt % 4 == 2:
                x += 1
                y -= 1
            elif cnt % 4 == 3:
                x += 1
                y += 1
            cnt += 1
    # 출력
    print(f'#{num+1}')
    for i in snail:
        for j in i:
            print(j, end=' ')
        print()

