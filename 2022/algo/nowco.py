import sys

N = int(sys.stdin.readline())
dic = {0:0,1: 1, 2: 1, 3: 2}


def arrmux(n1, n2):
    # return [[arr1[0][0] * arr2[0][0] + arr1[0][1] * arr2[1][0], arr1[0][0] * arr2[1][0] + arr1[0][1] * arr2[1][1]],
    #         [arr1[1][0] * arr2[0][0] + arr1[1][1] * arr2[1][0], arr1[1][0] * arr2[1][0] + arr1[1][1] * arr2[1][1]]]
    return mux(n1 + 1) * mux(n2) + mux(n1) * mux(n2 - 1)

def arr2(n):
    return [[]]

def mux(n):
    if n not in dic:
        if n % 2:
            dic[n] = mux(arrmux(n // 2,n // 2) + 1)
        else:
            dic[n] = arrmux(n // 2, n // 2)
    return dic[n]

print(mux(N))
print(dic)
# print(mux(N) % 1000000)
