T = int(input())
for _ in range(T):
    arr = [0] * 5
    mxarr = 0
    for __ in range(5):
        arr[__] = input()
        if mxarr < len(arr[__]):
            mxarr = len(arr[__])
    for ___ in range(5):
        while len(arr[___]) < mxarr:
            arr[___] += ' '
    ans = ''
    for i in range(mxarr):
        for j in range(5):
            ans += arr[j][i]
    ans = ''.join(k for k in ans if k !=' ')
    print(f'#{_ + 1} {ans}')
