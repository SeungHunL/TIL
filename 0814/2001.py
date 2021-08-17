def smash(map, a, b, k):
    kill = 0
    for p in range(k):
        for q in range(k):
            kill += map[a + p][b + q]
    return kill


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    bingo = [0] * N
    for x in range(N):
        bingo[x] = list(map(int, input().split()))
    death = max = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            death = smash(bingo, i, j, M)
            if max < death:
                max = death
    print(f'#{_ + 1} {max}')
