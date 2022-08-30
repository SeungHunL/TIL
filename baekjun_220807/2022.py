import sys

input = sys.stdin.readline

x, y, c = map(float, input().split())


def func(a, b, c):
    x1 = (a ** 2 - c ** 2) ** (0.5)
    y1 = (b ** 2 - c ** 2) ** (0.5)
    r = x1 * y1 / (y1 + x1)
    return r
s=0
e=min(x,y)
res=0
while e-s>0.000001:
    m = (s + e) / 2
    if func(x,y,m)>=c:
        res=m
        s=m
    else:
        e=m
print(f'{res:.3f}')
