import sys

N, r, c = map(int, sys.stdin.readline().split())
s = 0
while N > 1:
    if r < 2 ** (N - 1):
        if c < 2 ** (N - 1):
            s = s
        else:
            s += 2 ** (2 * (N - 1))
            c -= 2 ** (N - 1)
    else:
        r -= 2 ** (N - 1)
        if c < 2 ** (N - 1):
            s += 2 * 2 ** (2 * (N - 1))
        else:
            s += 3 * 2 ** (2 * (N - 1))
            c -= 2 ** (N - 1)
    N -= 1

print(2 * r + c + s)
