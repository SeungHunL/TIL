import sys

input = sys.stdin.readline

N =int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
conA=[0]*N
conB=B[:]
A.sort(reverse=True)
for i in range(N):
    mB=max(conB)
    idxmB=conB.index(mB)
    conB[idxmB]=-1
    conA[idxmB]=A.pop()
ans=0
for i in range(N):
    ans+=conA[i]*B[i]
print(ans)


