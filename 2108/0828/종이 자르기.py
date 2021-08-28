import sys

w, h = map(int, sys.stdin.readline().split())
x,y=[0],[0]
for _ in range(int(sys.stdin.readline())):
    b,v = map(int, sys.stdin.readline().split())
    if b==0:
        y.append(v)
    else:
        x.append(v)
x.append(w)
y.append(h)
x.sort()
y.sort()
mx=my=0
for i in range(1,len(x)):
    if mx<x[i]-x[i-1]:
        mx=x[i]-x[i-1]
for i in range(1,len(y)):
    if my<y[i]-y[i-1]:
        my=y[i]-y[i-1]
print(mx*my)