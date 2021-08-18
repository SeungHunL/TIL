def pascal(a):
    parlist = [0] * a
    for k in range(a):
        parlist[k] = [0] * (k + 1)
    for i in range(a):
        for j in range(i + 1):
            if j == 0:
                parlist[i] = [1]
            elif j == i:
                parlist[i].append(1)
            else:
                parlist[i].append(parlist[i - 1][j - 1] + parlist[i - 1][j])
        for l in range(i + 1):
            print(parlist[i][l], end=" ")
        print()


T = int(input())
for _ in range(T):
    print(f'#{_ + 1}')
    pascal(int(input()))