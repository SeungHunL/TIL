import sys


def square():
    ans = 0
    for i in range(N - 1):
        for j in range(M - 2):
            arr = [maps[i][j], maps[i][j + 2], maps[i + 1][j], maps[i + 1][j + 2]]
            arr1 = [maps[i][j], maps[i][j + 1], maps[i][j + 2]]
            arr2 = [maps[i + 1][j], maps[i + 1][j + 1], maps[i + 1][j + 2]]

            ans = max(ans,
                      sorted(arr1)[-1] + sum(arr2),
                      sorted(arr2)[-1] + sum(arr1),
                      sum(sorted(arr)[2:]) + maps[i][j + 1] + maps[i + 1][j + 1])
    for i in range(N - 2):
        for j in range(M - 1):
            arr = [maps[i][j], maps[i][j + 1], maps[i + 2][j], maps[i + 2][j + 1]]
            arr1 = [maps[i][j], maps[i + 1][j], maps[i + 2][j]]
            arr2 = [maps[i][j + 1], maps[i + 1][j + 1], maps[i + 2][j + 1]]
            ans = max(ans,
                      sorted(arr1)[-1] + sum(arr2),
                      sorted(arr2)[-1] + sum(arr1),
                      sum(sorted(arr)[2:]) + maps[i + 1][j] + maps[i + 1][j + 1])

    return ans


def four():
    ans = 0
    for i in range(N - 3):
        for j in range(M):
            ans = max(ans, maps[i][j] + maps[i + 1][j] + maps[i + 2][j] + maps[i + 3][j])
    for i in range(N):
        for j in range(M - 3):
            ans = max(ans, maps[i][j] + maps[i][j + 1] + maps[i][j + 2] + maps[i][j + 3])
    return ans


input = sys.stdin.readline

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
print(max(four(), square()))
