T = int(input())
for num in range(T):
    N, K = map(int, input().split())
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    ans = 0

    for i in range(1, 1 << 12):
        s = 0
        cnt = 0
        for j in range(13):
            if i & (1 << j):
                s += A[j]
                cnt += 1

        if s == K and cnt == N:
            ans += 1

    print(f'#{num + 1} {ans}')
