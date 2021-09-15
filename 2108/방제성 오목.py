for _ in range(int(input())):
    N = int(input())
    map = []
    flag = 0
    for __ in range(N): map.append(input())
    for i in range(N):
        for j in range(N):
            if map[i][j] == 'o':
                if j + 4 <= N - 1:
                    for k in range(1, 5):
                        if map[i][j + k] != 'o':
                            break
                    else:
                        flag = 1
                        break
                    if i + 4 <= N - 1:
                        for m in range(1, 5):
                            if map[i + m][j + m] != 'o':
                                break
                        else:
                            flag = 1
                            break
                if i + 4 <= N - 1:
                    for l in range(1, 5):
                        if map[i + l][j] != 'o':
                            break
                    else:
                        flag = 1
                        break
                    if 0 <= j - 4:
                        for n in range(1, 5):
                            if map[i + n][j - n] != 'o':
                                break
                        else:
                            flag = 1
                            break
    ans = 'YES' if flag else 'NO'
    print(f'#{_ + 1} {ans}')

