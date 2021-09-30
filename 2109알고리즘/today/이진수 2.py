for _ in range(int(input())):
    N=float(input())
    print(f'#{_ + 1} ',end='')
    i=1
    ans=''
    while N:
        if N-2**(-i)>=0:
            ans+='1'
            if N-2**(-i)==0:
                print(ans)
                break
            N-=2**(-i)
        else:
            ans+='0'
        i+=1
        if i==13:
            print('overflow')
            break
