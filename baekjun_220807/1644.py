import sys

input = sys.stdin.readline
N=int(input())
a=[False,False]+[True]*(N-1)
primes=[]
for i in range(2,N+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i,N+1,i):
            a[j]=False
ans=0
if N>1 and primes[-1]==N:
    ans+=1
for i in range(len(primes)):
    for j in range(i+1,len(primes)):
        a=sum(primes[i:j])
        if a>N:
            break
        elif a==N:
            ans+=1
print(ans)