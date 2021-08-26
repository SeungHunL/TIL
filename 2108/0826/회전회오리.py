for _ in range(int(input())):
    N,M =map(int,input().split())
    Maps=list(map(int,input().split()))
    i= M % N
    print(f'#{_+1} {Maps[i]}')