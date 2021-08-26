for _ in range(int(input())):
    N = int(input())
    map = []
    ans = 0
    for __ in range(N): map.append(input())
    for i in range(N):
        for j in range(N):
            if j<N-6 and map[i][j:j + 5] == 'ooooo':
                ans = 1
                break
            elif j<N-6 and map[j:j+5][i] == 'ooooo':
                ans = 1
                break
            elif for
        if ans:
            break
    else:
        print(f'{_ + 1} {ans}')
