for tc in range(int(input())):
    N, K = map(int, input().split())
    nums = input()
    siz = N // 4
    ndic = set()
    for i in range(siz):
        n1 = int(nums[:siz], 16)
        n2 = int(nums[siz:siz * 2], 16)
        n3 = int(nums[siz * 2:siz * 3], 16)
        n4 = int(nums[siz * 3:], 16)
        nums = nums[1:] + nums[0]
        ndic.add(n1)
        ndic.add(n2)
        ndic.add(n3)
        ndic.add(n4)
    ndic=list(set(ndic))
    ndic.sort(reverse=True)

    print(f'#{tc} {ndic[K-1]}')
