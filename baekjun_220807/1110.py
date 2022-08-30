import sys
input = sys.stdin.readline

N= int(input())
t=N
if t < 10:
    a = 0
    b = t
    c = (a + b) % 10
    t = b * 10 + c
else:
    if t % 10:
        a = t // 10
        b = t % 10
        c = (a + b) % 10
        t = b * 10 + c
    else:
        t //= 10
cnt=1
while N!=t:
    if t < 10:
        a = 0
        b = t
        c = (a + b) % 10
        t = b * 10 + c
    else:
        if t % 10:
            a = t // 10
            b = t % 10
            c = (a + b)%10
            t = b * 10 + c
        else:
            t//= 10
    cnt+=1
print(cnt)