import sys
input = sys.stdin.readline

N= int(input())
points=[]
for i in range(N):
    points.append(tuple(map(int,input().split())))
points.append(points[0])
ans=0
sa=sb=0
for i in range(N):
    sa+=points[i][0]*points[i+1][1]
    sb+=points[i][1]*points[i+1][0]

print(round(abs(sa-sb)/2,1))