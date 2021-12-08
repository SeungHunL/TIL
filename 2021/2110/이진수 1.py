T=int(input())
for _ in range(T):
    N,M=input().split()
    print(f'#{_ + 1}',end=' ')
    for i in range(int(N)):
        print(format(int('0x' + M[i], 16), '04b'),end='')
    print()