A = list(map(int,input().split()))
for i in range(len(A)):
    for j in range(i,len(A)):
        if A[i] <= A[j]:
            A[j],A[i] = A[i],A[j]
print(A[1])