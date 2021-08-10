for num in range(10):
    N = int(input())
    Num_list = list(map(int, input().split()))
    for i in range(0, len(Num_list) - 1):
        for j in range(i + 1, len(Num_list)):
            if Num_list[i] > Num_list[j]:
                Num_list[i], Num_list[j] = Num_list[j], Num_list[i]
    # 정렬
    for maxl in range(Num_list[-1], 1, -1):

        block = 0
        for j in range(0, len(Num_list)):
            if Num_list[j] > maxl:
                block += Num_list[j] - maxl
        if block > N:
            mx = maxl+1
            break
    # 최대
    for minl in range(0, Num_list[-1], +1):
        block = 0
        for k in range(0, len(Num_list)):
            if minl > Num_list[k]:
                block += minl - Num_list[k]
        if block > N:
            mn = minl-1
            break
    # 최소
    print(f'#{num + 1} {mx-mn}')
