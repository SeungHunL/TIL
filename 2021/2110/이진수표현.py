T=int(input())
for _ in range(T):
    N,M=map(int,input().split())
    print(f'#{_+1}', 'ON' if format(M,'0'+f'{N}'+'b')[-N:]=='1'*N else 'OFF')