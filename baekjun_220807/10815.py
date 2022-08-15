import sys

input = sys.stdin.readline
N=int(input())
cs=set(map(int,input().split()))
M=int(input())
ls=list(map(int,input().split()))
ans=[]
for l in ls:
    if l in cs:
        ans.append('1')
    else:
        ans.append('0')
print(' '.join(ans))