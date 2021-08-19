T = int(input())
for _ in range(T):
    N = int(input())
    A = [0] * N
    count=[0]*200
    mx = 0
    for __ in range(N):
        x, y = map(int, input().split())
        if x < y:
            A[__] = [(x - 1) // 2, (y - 1) // 2 , 0]
        else:
            A[__] = [(y - 1) // 2, (x - 1) // 2 , 0]

    # A =  (작은 수, 큰 수)
    # 400개의 방은 복도 양 측에 200개씩 있으므로
    # 1,2번 방 앞을 하나의 지점으로 본다.
    for i in range(N):
        for j in range(A[i][0],A[i][1]+1):
            count[j] += 1
    for k in range(200):
        if mx< count[k]:
            mx = count[k]

    print(f'#{_ + 1} {mx}')
