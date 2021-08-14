T = int(input())
for _ in range(T):
    N = int(input())
    A = [0] * N
    ans = 0
    for __ in range(N):
        A[__] = set(map(int, input().split()))

    # result = []
    # for i in range(N):
    #     cnt = 0
    #     s = 0
    #     mx = 0
    #     for j in range(i+1,N):
    #         if A[j][0] > A[i][0] and A[j][1] > A[i][1]:
    #             s += 1
    #         elif A[j][0] < A[i][0] and A[j][1] < A[i][1]:
    #             s += 1
    #         else:
    #             cnt +=1
    #     A[i].append(cnt)
    #     A[i].append(s)
    #     if mx < cnt:
    #         ans = cnt
    print(A)

    print(f'#{_ + 1} {ans+1}')
