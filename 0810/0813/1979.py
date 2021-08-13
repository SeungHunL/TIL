T = int(input())
for _ in range(T):
    N, K = map(int,input().split())
    M = [[0] * N for __ in range(N)]
    for ___ in range(N):
        M[___] = list(map(int, input().split()))

    NL = [0] * (N+1)
    for i in range(N):
        x_cnt = y_cnt = 0
        for j in range(N):
            if M[i][j] == 1:
                x_cnt += 1
                if j == N - 1:
                    NL[x_cnt] += 1
                    x_cnt = 0
            elif M[i][j] == 0:
                NL[x_cnt] += 1
                x_cnt = 0

            if M[j][i] == 1:
                y_cnt += 1
                if j == N - 1:
                    print(y_cnt,j,i)
                    NL[y_cnt] += 1
                    y_cnt = 0
            elif M[j][i] == 0:
                print(y_cnt, j, i)
                NL[y_cnt] += 1
                y_cnt = 0
    print(NL)