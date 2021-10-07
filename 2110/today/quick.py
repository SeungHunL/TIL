def hoare(arr,l,r):
    p=arr[l]
    i=l
    j=r
    while i<=j:
        while i<=j and arr[i]<=p:
            i+=1
        while i<=j and arr[j]>=p:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j

def quick(arr,l,r):
    if l<r:
        s=hoare(arr,l,r)
        quick(arr,l,s-1)
        quick(arr,s+1,r)

for q in range(int(input())):
    N=int(input())
    T=list(map(int,input().split()))
    quick(T,0,N-1)
    print(f'#{q+1} {T[N//2]}')