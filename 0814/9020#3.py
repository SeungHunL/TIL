import sys


def prime_number(n):
    l = [2]
    for i in range(3, n + 1, 2):
        cnt = 0
        for j in range(3, i + 1):
            if i % j == 0:
                cnt += 1
        if cnt == 1:
            l.append(i)
    return l


def goldbach(b, bn):
    min = 10000
    for k in bn:
        if (b - k >= k) and ((b - k) in bn):
            if min > b - 2 * k:
                min = b - 2 * k
                km_s = k
                km_e = b - k
    print(km_s, km_e)


for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    pn = prime_number(N)
    goldbach(N, pn)
