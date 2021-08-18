def tar(a,b):
    if b==1:
        return a
    else:
        return a*tar(a,b-1)

for _ in range(10):
    T=int(input())
    A,B = map(int,input().split())
    print(f'#{_+1} {tar(A,B)}')