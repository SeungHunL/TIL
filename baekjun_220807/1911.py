import sys

input = sys.stdin.readline

N, L = map(int, input().split())
ws = []
for _ in range(N):
    ws.append(list(map(int, input().split())))
ws = sorted(ws, key=lambda x: x[0])
n = 0
c = 0
for i in ws:
    s, e = i[0], i[1]
    s=max(s,n+1)
    t = (e - s) // L
    if (e - s) % L:
        c += t + 1
        s += (t+1) * L
    else:
        c += t
        s += t * L
    n=s
    n-=1
print(c)