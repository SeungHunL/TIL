T = int(input())
for _ in range(T):
    N = int(input())
    A = [0] * N
    ans = 0

    for __ in range(N):
        x, y = map(int, input().split())
        if x > y:
            A[__] = [(x - 1) // 2, (y - 1) // 2 , 0]
        else:
            A[__] = [(y - 1) // 2, (x - 1) // 2 , 0]

    # A =  (작은 수, 큰 수)
    # 400개의 방은 복도 양 측에 200개씩 있으므로
    # 1,2번 방 앞을 하나의 지점으로 본다.

    front = 0
    for i in range(200):
        if front < A[i][0]:
            front_idx = i
    # 가장 앞에 있는 학생을 해결할 때  그 학생 이후에 더 가능한 사람이 있는지 확인
    front = A[front_idx][1] + 1
    for j in range(front,200):
        if front < A[j][0]:
            front_idx = j

    front = A[front_idx][1] +1

    for n in range(200):
        if A[n][2] == 0 :


    else:
        print(f'#{_ + 1} {ans+1}')
        break

    #     A[i].append(cnt)
    #     A[i].append(s)
    #     if mx < cnt:
    #         ans = cnt
    print(A)

    print(f'#{_ + 1} {ans+1}')
