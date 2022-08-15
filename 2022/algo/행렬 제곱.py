import sys


def mux(arr1, arr2):
    ans = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                ans[i][j] += arr1[i][k] * arr2[k][j]
            ans[i][j] %= 1000
    return ans


input = sys.stdin.readline
N, B = map(int, input().split())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

dp = [matrix]
binB = bin(B)[2:]
for _ in range(len(binB) - 1):
    if _ == 0:
        dp.append(mux(matrix, matrix))
    else:
        dp.append(mux(dp[-1], dp[-1]))

ans = dp[-1]
if len(binB) != 1:
    for _ in range(1, len(binB)):
        if binB[_] == '1':
            ans = mux(ans, dp[-_ - 1])
for i in range(N):
    for j in range(N):
        ans[i][j] %= 1000
for an in ans:
    print(' '.join(str(m) for m in an))
