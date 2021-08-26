N = int(input())
for num in range(N):
    L = int(input())
    A = list(map(int, input().split()))
    h = 0
    for i in range(L):
        high = 0
        for j in range(i+1, L):
            if A[i] > A[j]:
                high +=1
                break
            elif high < L - i and j==L-1:
                high = L - i
                print(L-i)
        if h<high:
            h= high
    print(f'#{num + 1} {h}')