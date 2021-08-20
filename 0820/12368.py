for _ in range(int(input())):
    N,M = map(int,input().split())
    ans =(N+M)//24
    print(f'#{_+1} {ans}')