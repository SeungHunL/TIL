def select(arr,n,s=0):
    if s==n-1:
        return
    t=s
    tv=arr[t]
    for i in range(s+1,len(arr)):
        if tv>arr[i]:
            t=i
            tv=arr[t]
    arr[s],arr[t]=tv,arr[s]
    select(arr,s+1)
    return arr

for i in range(int(input())):
    nums, t = input().split()
    nums = list(nums)
    use = [0] * len(nums)
    allcost=0

    print(f'#{i+1} {allcost}')