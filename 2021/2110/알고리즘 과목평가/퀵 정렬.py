def quickSort(arr,l,r):
    if l<r:
        s=part(arr,l,r)
        quickSort(arr,l,s-1)
        quickSort(arr,s+1,r)

def part(arr,l,r):
    print(arr)
    pivot=arr[l]
    i=l
    j=r
    while i<=j:
        while i<=j and arr[i]<=pivot:
            i+=1
        while i<=j and arr[j]>=pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j

arr=[3,2,4,6,9,1,8,7,5]
quickSort(arr,0,len(arr)-1)
print(arr)