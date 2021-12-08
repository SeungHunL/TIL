def Mergesort(arr):
    if len(arr)==1:
        return arr
    else:
        m=len(arr)//2
        return Merge(Mergesort(arr[:m]),Mergesort(arr[m:]))

def Merge(a1,a2):
    res=[]
    i=j=0

    while i<len(a1) and j<len(a2):
        if a1[i]<=a2[j]:
            res.append(a1[i])
            i+=1
        else:
            res.append(a2[j])
            j += 1
    if i<len(a1):
        res+=a1[i:]
    else:
        res+=a2[j:]
    return res


arr=[69,10,30,30,16,8,31,22]
arr=Mergesort(arr)
print(arr)