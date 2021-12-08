T = int(input())
for num in range(T):
    N = int(input())
    su = list(map(int,input().split()))
    for i in range(len(su)):
        min = i
        for j in range(i + 1, N):
            if su[min] > su[j]:
                min = j
        su[i], su[min] = su[min], su[i]
    print(f'#{num + 1}',end=' ')
    print(*su)
