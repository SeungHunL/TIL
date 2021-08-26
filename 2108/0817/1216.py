for _ in range(10):
    box = [0] * 100
    A=int(input())
    for __ in range(100):
        box[__] = input()
    C=0
    for i in range(100):
        for j in range(100):
            for M in range(10,30):
                if ((j + M - 1) <= 100 - 1) and (box[i][j] == box[i][j + M - 1]):
                    for l in range(1, M):
                        if box[i][j + l] != box[i][j + M - 1 - l]:
                            break
                    else:
                        if C<M:
                            C=M
                        break
                if ((j + M - 1) <= 100 - 1) and (box[j][i] == box[j + M - 1][i]):
                    for m in range(1, M):
                        if box[j + m][i] != box[j + M - 1 - m][i]:
                            break
                    else:
                        if C<M:
                            C=M
                        break

    print(f'#{_ + 1} {C}')