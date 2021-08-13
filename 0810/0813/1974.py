T = int(input())
for _ in range(T):
    N = [[0] * 9 for __ in range(9)]
    for n in range(9):
        N[n] = list(map(int, input().split()))
    cube = [0] * 10
    for k in range(3):
        for l in range(3):
            cube[N[k][l]] += 1
    if cube != [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
        print(f'#{_ + 1} 0')
        continue
    for i in range(9):
        galo = [0] * 10
        selo = [0] * 10
        for j in range(9):
            galo[N[i][j]] += 1
            selo[N[j][i]] += 1

        if galo != [0, 1, 1, 1, 1, 1, 1, 1, 1, 1] or selo != [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
            print(f'#{_ + 1} 0')
            break

    else:
        print(f'#{_ + 1} 1')

