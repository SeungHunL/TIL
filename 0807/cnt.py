N=int(input())
A=list(map(int,input().split()))
s=0
for i in range(2,len(A)):
    if A[i]>A[i-1]and A[i]>A[i-2]:
        if A[i]>A[i+1] and A[i]>A[i+2]:
            s += A[i]-max(A[i-2],A[i-1],A[i+1],A[i+2])
print(s)