def comb(arr, t, s=0):
    global allcost
    print(arr)
    for k in range(len(arr)-1):
        if arr[k]<arr[k+1]:
            break
    else:
        if flag or(t-s)%2==0:
            s=t
    if s == t:
        fin=int(''.join(arr))
        if allcost<=fin:
            allcost=fin
        return
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i!=j:
                s += 1
                arr[i],arr[j]=arr[j],arr[i]
                comb(arr, t, s)
                s -= 1
                arr[i], arr[j] = arr[j], arr[i]


for i in range(int(input())):
    nums, t = input().split()
    nums = list(nums)
    use = [0] * len(nums)
    allcost=0
    flag=0
    if len(nums)>len(set(nums)):
        flag=1
    comb(nums,int(t))
    print(f'#{i+1} {allcost}')