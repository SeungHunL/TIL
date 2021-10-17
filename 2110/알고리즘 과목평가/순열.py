def perm(n,k=0):
    if k==n:
        print(f)
    else:
        for i in range(k,n):
            swap(k,i)
            perm(n,k+1)
            swap(k,i)

def swap(a,b):
    f[a],f[b]=f[b],f[a]

def Subsets(n):
    ans=set()
    for num in range(1<<n):
        res=[]
        for i in range(n):
            if num & (1<<i):
                res.append(f'{arr[i]}')
        ans.add(''.join(res))
    print(ans)

def comb(n,r):
    if not r:
        print(t)
    elif n<r:
        return
    else:
        t[r-1]=arr[n-1]
        comb(n-1,r-1)
        comb(n-1,r)

def nCr(n,r,s,k):
    if k==r:
        return
    else:
        for i in range(s,n-r+k+1):
            com[k]=i
            nCr(n,r,i+1,k+1)


# f=[1,2,3]
# perm(len(f))

arr=[2,3,5,7,7,7]
Subsets(len(arr))
# t=[0]*4
# comb(len(arr),4)