import sys


def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        n = a % b
        a, b = b, n
    return a


input = sys.stdin.readline

A, B, x, y, p, q = map(int, input().split())
c = abs(q * x - p * y)
g = gcd(q * A, p * B)
if c == 0:
    n = p * B // g
    m = q * A // g
    print(n + m - 1)
else:
    a = q * A // g
    b = p * B // g
    c//=g
    if c<0:
        print(-1)
    else:
        n = m = 1
        while True:
            if a * n - b * m == c:
                break
            elif a * n - b * m > c:
                m += 1
            else:
                n += 1
        print(n+m-1)
        print(n,m)
