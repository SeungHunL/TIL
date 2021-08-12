T = int(input())
for num in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    El = ''
    for i in range(10):
        if i % 2 == 0:
            max = i
            for j in range(i + 1, N):
                if A[max] < A[j]:
                    max = j
            A[i], A[max] = A[max], A[i]
            El += f'{A[i]} '
        else:
            min = i
            for k in range(i + 1, N):
                if A[min] > A[k]:
                    min = k
            A[i], A[min] = A[min], A[i]
            El += f'{A[i]} '


    print(f'#{num+1} {El}')