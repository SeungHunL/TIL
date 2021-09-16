import sys
from collections import deque

input = sys.stdin.readline
N=int(input())
nodes = list(map(int,input().split()))
graph=[[]for _ in range(N)]
for i in  range(1,N):
    graph[nodes[i]].append(i)
cut=int(input())
que=deque()
que.append(cut)
graph[nodes[cut]].remove(cut)
while que:
    cut=que.popleft()
    for j in graph[cut]:
        que.append(j)
    graph[cut]=[]

for k in graph[0]:
    que.append(k)
cnt=0
while que:
    cut=que.popleft()
    if graph[cut]:
        for l in graph[cut]:
            que.append(l)
    else:
        cnt+=1
print(cnt)