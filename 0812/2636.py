N, M = map(int, input().split())
A = [[0] * M for _ in range(N)]
for n in range(N):
    A[n] = list(map(int, input().split()))      #input
cnt = 0
while 1:
    change = 0
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if A[i][j] == 1:
                cnt += 1
                change += 1
    if change == 0:                             # 1이 없을 때 그 전 변화량
        print(cnt)
        break
    for p in range(N):
        for q in range(M):
            if A[p][q] == 1:
                A[p][q] = 'c'
                y = p
                x = q
                print(p,q,A[p][q])
                while 1:
                    L = A[y][x - 1]
                    B = A[y + 1][x]
                    R = A[y][x + 1]
                    T = A[y - 1][x]
                    print(L,B,R,T)
                    if (L,B,R,T) in [('c',1,1,1),(1,'c',1,1),(1,1,'c',1),(1,1,1,'c')]:
                        A[y][x] = 1

                    if L == 1:
                        A[y][x - 1] = 'c'
                        x -= 1
                        print('L')
                    elif B == 1:
                        A[y + 1][x] = 'c'
                        y += 1
                        print('B')
                    elif R == 1:
                        A[y][x + 1] = 'c'
                        x += 1
                        print('R')
                    elif T == 1:
                        A[y - 11][x] = 'c'
                        y -= 1
                        print('T')
                    else:
                        break


                break

    print(A)
    break
    # print(p,q)
