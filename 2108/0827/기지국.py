def rebuild(a, b, c, pad, count):
    if pad[a + c][b] == 'H':
        pad[a + c][b] = 'X'
    if pad[a][b + c] == 'H':
        pad[a][b + c] = 'X'


for _ in range(int(input())):
    N = int(input())
    map = [['X'] * (N + 6) for __ in range(6)]
    for __ in range(N):
        map.insert(-3, ['X'] * 3 + list(input()) + ['X'] * 3)
    ans = 0
    for i in range(3, N + 3):
        for j in range(3, N + 3):
            if map[i][j] == 'A':
                for k in range(-1, 2):
                    rebuild(i, j, k, map, ans)
            elif map[i][j] == 'B':
                for k in range(-2, 3):
                    rebuild(i, j, k, map, ans)
            elif map[i][j] == 'C':
                for k in range(-3, 4):
                    rebuild(i, j, k, map, ans)
    for x in range(3, N + 3):
        for y in range(3, N + 3):
            if map[x][y] == 'H':
                ans += 1
    print(f'#{_ + 1} {ans}')
