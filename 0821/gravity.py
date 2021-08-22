for _ in range(int(input())):
    N=int(input())
    num=list(map(int,input().split()))

    mx = 0

    for i in range(N):
        count = 0
        for j in range(i,N):
            if num[i]>num[j]:
                count+=1
        mx = mx if mx > count else count
    print(mx)