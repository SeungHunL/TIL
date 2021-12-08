for _ in range(int(input())):
    N, M, K = map(int, input().split())
    time = list(map(int, input().split()))
    time.sort()
    for i in range(N):
        if time[i]//M*K-i<=0:
            print(f'#{_+1} Impossible')
            break
    else:print(f'#{_+1} Possible')