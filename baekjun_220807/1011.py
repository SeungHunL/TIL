import sys

input = sys.stdin.readline
for _ in range(int(input())):
    x,y=map(int,input().split())
    t=y-x
    dp=3
    l=2
    c=2
    while dp<t+1:
        dp+=l
        c+=1
        if c%2==0:
            l+=1
    if t>2:
        print(c)
    else:
        print(t)
