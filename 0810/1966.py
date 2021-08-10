N = int(input())
for num in range(N):
    L = int(input())
    A = list(map(int,input().split()))
    for j in range(L-1):
        for i in range(L-j-1):
            if A[i]>A[i+1]:
                A[i],A[i+1] = A[i+1],A[i]
    l=''
    for c in range(len(A)):
        l += str(A[c])+' '
        if c==len(A):
            l-=' '
    print(f'#{num+1} {l}')