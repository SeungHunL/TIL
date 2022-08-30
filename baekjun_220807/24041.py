import sys
def func(s,x,L):
    return s*max(1,x-L)
input = sys.stdin.readline
N,G,K = map(int, input().split())
f1=[]
f2=[]
ss=0
for _ in range(N):
    S,L,O=map(int,input().split())
    if O==1:
        f1.append([S,L])
    else:
        f2.append([S,L])
        ss+=S
s=0
e=int(2e9)
res=0
while e-s>=0:
    m=(s+e)//2
    ans=0
    c = []
    for i in f1:
        c.append(func(i[0],m,i[1]))
    for i in f2:
        ans+=func(i[0],m,i[1])
    c.sort()
    ans+=sum(c[:len(c)-K])
    if ans>G:
        e=m-1
    else:
        res=m
        s=m+1
print(res)