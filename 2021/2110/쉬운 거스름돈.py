for q in range(int(input().strip())):
    n = int(input().strip())
    m = [50000,10000,5000,1000,500,100,50,10]
    ans = ['0']*8
    i=0
    while n:
        ans[i]=str(n//m[i])
        n%=m[i]
        i+=1

    print(f'#{q+1}')
    print(' '.join(ans))