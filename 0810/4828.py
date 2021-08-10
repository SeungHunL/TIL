T = int(input().strip())
for num in range(T):
    N = int(input().strip())
    A = list(map(int,input().split()))
    MX = Mn = 0
    for i in range(0,len(A)):
        print(Mx,A[i])
        if MX < A[i]:
            Mx = A[i]
        if Mn == 0:
            Mn = A[i]
        elif Mn > A[i]:
            Mn = A[i]
    print(f'#{num+1} {Mx-Mn}')