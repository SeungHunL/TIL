for _ in range(int(input())):
    N = int(input())
    farm = []
    for __ in range(N):
        farm.append(input())
    harvest = 0
    for i in range(N):
        for j in range(N):
            if ((N - 1) / 2 - i <= j <= (N - 1) / 2 + i) and i <= (N - 1) / 2 :
                harvest += int(farm[i][j])

            elif (-(N - 1) / 2 + i <= j <= 3*(N - 1) / 2 - i) and i > (N - 1) / 2 :
                harvest += int(farm[i][j])
                print(i,j)
    print(f'#{_ + 1} {harvest}')
