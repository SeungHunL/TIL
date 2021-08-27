for _ in range(int(input())):
    N = int(input())
    Aset = list(map(int, input().split()))
    mx = -1
    for i in range(N):
        for j in range(i + 1, N):

            num = list(str(Aset[i] * Aset[j]))
            for k in range(1,len(num)):
                if num[k]<num[k-1]:
                    break
            else:
                if mx < Aset[i] * Aset[j]:
                    mx = Aset[i] * Aset[j]
    print(f'#{_ + 1} {mx}')
