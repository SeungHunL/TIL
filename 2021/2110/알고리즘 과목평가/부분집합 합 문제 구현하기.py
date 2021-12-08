def comb(n,k):
    if not k:
        if not sum(t):
            print(t)
        return
    elif n<k:
        return
    else:
        t[k-1]=arr[n-1]
        comb(n-1,k-1)
        comb(n-1,k)
arr=[-1,3,-9,6,7,-6,1,5,4,2]

for i in range(1,len(arr)):
    t = [0] * i
    comb(len(arr),i)