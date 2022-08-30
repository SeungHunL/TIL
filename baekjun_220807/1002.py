import sys

input = sys.stdin.readline
for _ in range(int(input())):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    ans=0
    a=(x2-x1)**2+(y2-y1)**2
    b=(r2+r1)**2

    if a==0:
        if r2==r1:
            print(-1)
        else:
            print(0)
    elif a==(r2-r1)**2:
        print(1)
    elif a<(r2-r1)**2:
        print(0)
    elif a>b:
        print(0)
    elif a==b:
        print(1)
    else:
        print(2)