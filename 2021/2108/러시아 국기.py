for _ in range(int(input())):
    N, M = map(int, input().split())
    flag = []
    for __ in range(N):
        flag.append(list(input()))
    mx = 0
    color = [[0] * 3 for k in range(N)]
    for i in range(N):
        for j in range(M):
            if flag[i][j] == 'W':
                color[i][0] += 1
            elif flag[i][j] == 'B':
                color[i][1] += 1
            else:
                color[i][2] += 1

    mn = 10000
    for n in range(1,N):
        for l in range(n + 1, N):
            W = B = R = 0
            for k in range(n):
                W += color[k][0]
            for v in range(n, l):
                B += color[v][1]
            for w in range(l, N):
                R += color[w][2]
            if mn > N * M - W - B - R:
                mn = N * M - W - B - R
    print(f'#{_+1} {mn}')
