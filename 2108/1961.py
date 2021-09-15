T = int(input())
for _ in range(T):
    N = int(input())
    cube = [0] * N
    for __ in range(N):
        cube[__] = list(map(int, input().split()))
    tri_cube = [''] * N

    for i in range(N):                                          #90도
        for j in range(N):
            tri_cube[i] += str(cube[N - 1 - j][i])
        tri_cube[i] += ' '

    for i in range(N):                                          #180도
        for j in range(N):
            tri_cube[i] += str(cube[N - 1 - i][N - 1 - j])
        tri_cube[i] += ' '

    for i in range(N):                                          #270도
        for j in range(N):
            tri_cube[i] += str(cube[j][N - 1 - i])

    print(f'#{_+1}')                                              #출력
    for i in range(N):
        print(tri_cube[i])
