import sys
input = sys.stdin.readline
N=int(input())
aa=0
ans=0
a=N//2
while a>0:
    n=N-a
    for b in range(a,0,-1):
        c=n-b
        if c>b:
            break
        if a==b+c:
            continue
        ans+=1
    a-=1
print(ans)