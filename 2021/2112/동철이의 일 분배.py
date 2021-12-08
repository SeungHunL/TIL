def perm(n,k=0):
    if k==n:
        cal(f)
    else:
        for i in range(k,n):
            swap(k,i)
            perm(n,k+1)
            swap(k,i)

def swap(a,b):
    f[a],f[b]=f[b],f[a]

def cal(arr):
    global result
    ans=100
    for idx,r in enumerate(arr):
        ans*=chance[idx][r]*0.01
        if ans<float(result):
            return
    result=f'{ans:.6f}'

for tc in range(int(input())):
    N=int(input())
    chance=[]
    result=0
    for n in range(N):
        chance.append(list(map(int,input().split())))
    f=[]
    for i in range(N):
        f.append(i)
    perm(N)
    print(f'#{tc+1} {result}')