T = int(input())
for _ in range(T):
    N = int(input())
    bus = [0] * N
    for n in range(N):
        bus[n] = list(map(int, input().split()))
    P = int(input())

    C = [0] * (P)
    CNT = [0] * (5000)

    for __ in range(P):
        C[__] = int(input())
    C_set = list(set(C))
    # C번 버스 정류장 리스트                     #################################리스트로 실패함
    for i in range(N):
        for j in C_set:####

            if (j >= bus[i][0]) and (bus[i][1] >= j):
                CNT[j] += 1
    print('#{}'.format(_ + 1), end=' ')
    for val in C:
        print("{}".format(CNT[val]), end=" ")
    print()