T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    box = [0] * N
    for __ in range(N):
        box[__] = input()
    for i in range(N):
        for j in range(N):
            if ((j + M - 1) <= N - 1) and (box[i][j] == box[i][j + M - 1]):
                for l in range(1, M):
                    if box[i][j + l] != box[i][j + M - 1 - l]:
                        break
                else:
                    print(f'#{_ + 1}', end=" ")
                    for k in range(M):
                        print(box[i][j + k], end="")
                    print()
                    break

            if (j + M - 1) <= N - 1 and box[j][i] == box[j + M - 1][i]:
                for m in range(1, M):
                    if box[j + m][i] != box[j + M - 1 - m][i]:
                        break
                else:
                    print(f'#{_ + 1}', end=" ")
                    for k in range(M):
                        print(box[j + k][i], end="")
                    print()
                    break

