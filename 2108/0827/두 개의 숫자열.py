for _ in range(int(input())):
    N, M = map(int,input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    max_s = 0
    if N >= M:
        for i in range(N - M + 1):
            s = 0
            for j in range(M):
                s += A[j+i] * B[j]
            if max_s < s: max_s = s
    else:
        for i in range(M - N + 1):
            s = 0
            for j in range(N):
                s += A[j] * B[j+i]
            if max_s < s: max_s = s
    print(f'#{_+1} {max_s}')