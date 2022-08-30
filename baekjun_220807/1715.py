import sys
import heapq

input= sys.stdin.readline

N=int(input())
ns=[]
for i in range(N):
    heapq.heappush(ns,int(input()))
ans=0
while len(ns)>1:
    a=heapq.heappop(ns)
    b=heapq.heappop(ns)
    c=a+b
    heapq.heappush(ns,c)
    ans+=c
print(ans)