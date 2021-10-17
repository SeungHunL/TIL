import time
def perm(n,r=0):
    global aaa
    if r==n:
        aaa=list(map(str,aaa))
        ans.add(''.join(aaa))
        return
    else:
        for i in range(r,n):
            swap(i,r)
            perm(n,r+1)
            swap(i,r)

def swap(a,b):
    aaa[a],aaa[b]=aaa[b],aaa[a]

def perm2(n,k=0):
    if k==n:
        return
    else:
        for i in range(n):
            p[k]=aaa[i]
            used[i]=1
            perm(n,k+1)
            used[i]=0

for i in range(4):
    start=time.time()
    aaa=list(map(int,list(input())))
    ans=set()
    # perm(len(aaa))
    used=[0]*len(aaa)
    p=[0]*len(aaa)
    perm2(len(aaa))
    print(time.time()-start)