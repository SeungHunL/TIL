import sys

N = int(sys.stdin.readline())
a = [[1, 1], [1, 0]]
dic = {1: [[1,1],[1,0]]}


def arrmux(arr1, arr2):
    return [[arr1[0][0] * arr2[0][0] + arr1[0][1] * arr2[1][0], arr1[0][0] * arr2[1][0] + arr1[0][1] * arr2[1][1]],
            [arr1[1][0] * arr2[0][0] + arr1[1][1] * arr2[1][0], arr1[1][0] * arr2[1][0] + arr1[1][1] * arr2[1][1]]]


def mux(n):
    if n not in dic:
        if n % 2:
            dic[n] = arrmux(arrmux(mux(n // 2),mux(n // 2)),a)
        else:
            dic[n] = arrmux(mux(n // 2),mux(n // 2))
    return dic[n]


print(mux(N%1500000)[0][1] % 1000000)