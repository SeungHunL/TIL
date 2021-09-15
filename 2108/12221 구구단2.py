for _ in range(int(input())):
    A,B=map(int,input().split())
    if A<10 and B<10:
        print(f'#{_+1} {A*B}')
    else:
        print(f'#{_+1} -1')