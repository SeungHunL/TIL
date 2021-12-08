
def select(arr,s=0):
    N=len(arr)
    if s==N-1:
        return
    t=s
    tv=arr[t]
    for i in range(s+1,N):
        if tv>arr[i]:
            t=i
            tv=arr[t]
    arr[s],arr[t]=tv,arr[s]
    select(arr,s+1)
    return arr


print(select([4,5,2,3,1]))