T = int(input())
for num in range(T):
    N = int(input())
    M = []
    B = [[0] * 10 for _ in range(10)]
    for n in range(N):
        M = (list(map(int, input().split())))
        for i in range(M[0], M[2] + 1):
            for j in range(M[1], M[3] + 1):
                B[i][j] += M[4]

    ans = 0
    for i in range(10):
        for j in range(10):
            if B[i][j] == 3:
                ans += 1
    print(f'#{num + 1} {ans}')
