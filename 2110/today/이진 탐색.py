def bfind(arr, l,h,n):
    global a,b,c
    if l>h:
        return
    else:
        m = (l+h) // 2
        if n == arr[m]:
            c+=1
            return
        elif n < arr[m]and not a:
            a=1
            b=0
            bfind(arr,l,m-1, n)
        elif n > arr[m]and not b:
            a=0
            b=1
            bfind(arr,m+1,h, n)


for q in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    B.sort()
    c=0
    for i in B:
        a,b=0,0
        bfind(A,0,N-1, i)
    print(f'#{q + 1} {c}')
