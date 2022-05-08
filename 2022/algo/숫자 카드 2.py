import sys
input = sys.stdin.readline

N=int(input())
arr = list(map(int,input().split()))
M=int(input())
arr2 = list(map(int,input().split()))
ad = {}
for i in arr:
    if i in ad:
        ad[i] +=1
    else:
        ad[i] =1
for i in arr2:
    if i in ad:
        print(ad[i],end=' ')
    else:
        print(0,end=' ')