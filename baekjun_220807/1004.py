import sys

input = sys.stdin.readline
for _ in range(int(input())):
    x1,y1,x2,y2=map(int,input().split())
    ans=0
    for _ in range(int(input())):
        x,y,r=map(int,input().split())
        t=0
        if (x-x1)**2+(y-y1)**2<r**2:
            t+=1
        if (x-x2)**2+(y-y2)**2<r**2:
            t+=1
        if t==2:
            pass
        elif t:
            ans+=1
    print(ans)