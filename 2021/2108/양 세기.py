for _ in range(int(input())):
    N=int(input())
    check=[0]*10
    n=1
    while 1 :
        solo=N*n
        for i in set(str(solo)):
            if not check[int(i)]:
                check[int(i)]=1
        if not check.count(0):
            break
        n+=1
    print(f'#{_+1} {solo}')