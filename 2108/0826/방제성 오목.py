for _ in range(int(input())):
    N = int(input())
    map = []
    ans = 0
    for __ in range(N): map.append(input())
    for i in range(N):
        for j in range(N):
            if map[i][j]=='o':
                if j+5<=N-1:
                    for k in range(1,5):
                        if map[i][j+k]!='o':
                            break
                    else:
                        flag=1
                        break
                if i+5<=N-1:
                    for l in range(1,5):
                        if map[i+l][j]!='o':
                            break
                    else:
                        flag=1
                        break

        print(f'{_ + 1} {ans}')
