import sys

input= sys.stdin.readline

N=int(input())
ns=list(map(int,input().split()))
ans=[0]
for i in range(1,N):
    l=ns[i]
    for j in range(i-1,-1,-1):
        if ns[j]>=l:
            ans.append(j+1)
            break
    else:
        ans.append(0)
print(' '.join(list(map(str,ans))))