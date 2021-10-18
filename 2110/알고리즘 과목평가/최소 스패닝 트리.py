import sys
input=sys.stdin.readline

V,E=map(int,input())
al=[]
for i in range(E):
    al.append(list(map(int,input().split())))
al.sort(key=lambda x:x[2])