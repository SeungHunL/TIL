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
            swap(arr,i,j)
    swap(arr,l,j)
    return j

def quick(arr,l,r):
    if l<r:
        s=hoare(arr,l,r)
        quick(arr,l,s-1)
        quick(arr,s+1,r)

def swap(arr,a,b):
    arr[a],arr[b]=arr[b],arr[a]

A=[11,45,23,81,28,34]
C=[1,1,1,0,0]
B=[3,1,4,6,9,2,8,7,5]
quick(C,0,len(C)-1)
print(C)