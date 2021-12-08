def SelectionSort(A):
    n=len(A)
    for i in range(0,n-1):
        minI=i
        for j in range(i+1,n):
            if A[j]<A[minI]:
                minI=j
        A[minI],A[i]=A[i],A[minI]

def SelectionSort2(A):
    if A != []:
        s=min(A)
        A.remove(s)
        return [s]+SelectionSort2(A)
    else:
        return []
print(SelectionSort2([1,56,2,6,3]))