T = int(input())
for _ in range(T):
    N, Q = map(int,input().split())
    boxbox = [0]*N
    for n in range(Q):
        L, R = map(int,input().split())
        for i in range(L-1,R):
            boxbox[i] = (n+1)
    print(f'#{_+1}', end = ' ' )
    for j in range(N):
        print('{}'.format(boxbox[j]),end = ' ')
    print()