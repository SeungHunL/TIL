for _ in range(int(input())):
    N = int(input())
    maps = [[0] * N for __ in range(N)]
    s = 1
    y = 0
    x = -1
    p = 1
    while 1:
        for i in range(N):
            x += p
            maps[y][x] = s
            s += 1
        N -= 1
        if N == 0: break
        for j in range(N):
            y += p
            maps[y][x] = s
            s += 1
        p *= -1
    print(f'#{_ + 1}')
    for k in maps:
        print(' '.join(map(str, k)))
