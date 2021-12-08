def select(arr, t,sorti=0, s=0,used=[]):
    global allcost
    # 종료 조건
    for k in range(sorti + 1, len(arr)):
        if arr[k] > arr[k - 1]: break
    else:
        if not (flag or (t - s) % 2 == 0):
            arr[-1], arr[-2] = arr[-2], arr[-1]
        s = t
    if s == t:
        allcost = int(''.join(arr))
        return
    # 연산
    top = sorti
    while 1:
        topvalue = arr[sorti]
        for i in range(sorti + 1, len(arr)):
            if topvalue <= arr[i]: top, topvalue = i, arr[i]
        if top != sorti:
            break
        else:
            sorti += 1
    arr[sorti], arr[top] = arr[top], arr[sorti]
    # 같은 수의 교환이 연속 될 때 더 큰 값으로 정렬
    if used:
        if used[0]==arr[sorti]:
            used.append(top)
            for l in range(1,len(used)):
                for m in range(l+1,len(used)):
                    if used[l]>used[m] and arr[used[l]]>arr[used[m]]:
                        arr[used[l]],arr[used[m]]=arr[used[m]],arr[used[l]]
        else:
            used=[arr[sorti],top]
    else:
        used=[arr[sorti],top]
    select(arr, t,sorti + 1, s + 1,used)


for i in range(int(input())):
    nums, time = input().split()
    nums = list(nums)
    allcost = 0
    flag = 1 if len(nums) > len(set(nums)) else 0
    select(nums,int(time))
    print(f'#{i + 1} {allcost}')
