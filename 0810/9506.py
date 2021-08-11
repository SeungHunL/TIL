while 1:
    N = int(input())
    if N == -1:
        break
    l = ''
    s = 1
    for i in range(2, N):
        if N % i == 0:
            l += f' + {i}'
            s += i
    if s == N:
        print(f'{N} = 1{l}')
    else:
        print(f'{N} is NOT perfect.')
