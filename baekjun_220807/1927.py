import sys
import heapq

input= sys.stdin.readline

N=int(input())
ns=[]
for i in range(N):
    s=int(input())
    if s==0:
        if ns:
            a = heapq.heappop(ns)
            print(a)
        else:
            print(0)
    else:
        heapq.heappush(ns,s)