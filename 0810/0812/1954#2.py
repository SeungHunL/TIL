# 입력
T = int(input())
for num in range(T):
    N = int(input())
    snail = [[0] * N for _ in range(N)]
    # 빈 2차원 리스트 생성
    cnt = N
    (x, y,k,s) = (-1, 0,0,2)
    for c in range(cnt):
        for a in range(cnt):
            k += 1
            x += (-1) ** s
            snail[y][x] = k
        cnt -= 1
        for b in range(cnt):
            k += 1
            y -= (-1) ** (s+1)
            snail[y][x] = k
        s+=1

    # 출력
    print(f'#{num + 1}')
    for i in snail:
        for j in i:
            print(j, end=' ')
        print()
