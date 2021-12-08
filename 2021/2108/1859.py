T = int(input())
for _ in range(T):
    N = int(input())
    K = list(map(int, input().split()))
    benefit = 0
    # setting
    while 1:
        h = 0
        hidx = 0

        for i in range(1,len(K)):
            if h < K[i]:
                h = K[i]
                hidx = i
        # 최고점 찾기
        if hidx == 0:
            break

        for j in range(hidx):
            if K[hidx] > K[j]:
                benefit += K[hidx] - K[j]

        # 최고점에서의 이득 구하기
        else:
            K = K[hidx + 1:]
        # 최고점 이후의 리스트
    # 최대 이득 찾기
    print(f'#{_ + 1} {benefit}')
