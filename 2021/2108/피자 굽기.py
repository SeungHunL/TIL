for _ in range(int(input())):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))

    pz = [0] * N
    pz_idx = [0] * N
    pz_count = 0
    for __ in range(N):
        if Ci:
            pz[__] = Ci.pop(0)
            pz_idx[__] = __
            pz_count += 1

    i = -1
    while 1:
        i += 1
        i %= N
        if pz.count(0) == N-1:
            for k in range(N):
                if pz[k] > 0:
                    ans = k
                    break
            break                   # 탈출 조건
        pz[i] //= 2                 # 확인 하면서 반절
        if pz[i] == 0 and Ci:
            pz[i] = Ci.pop(0)
            pz_idx[i] = pz_count
            pz_count += 1           # 들어간 피자의 인덱스 처리

    print(f'#{_ + 1} {pz_idx[ans] + 1}')
