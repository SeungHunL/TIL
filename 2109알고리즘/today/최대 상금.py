def comb(arr, t, s=0):
    global allcost
    print(allcost,arr)
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
    comb(nums,int(t))
    print(f'#{i+1} {allcost}')