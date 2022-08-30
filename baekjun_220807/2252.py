import sys
from collections import deque
input = sys.stdin.readline
N,M=map(int,input().split())
gcnt=[0]*(N+1)
nex=deque()
board=[[]for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    board[a].append(b)
    gcnt[b]+=1
que=[]
for i in range(1,N+1):
    if gcnt[i]==0:
        nex.append(i)
while len(que)<N:
    i=nex.popleft()
    que.append(str(i))
    if board[i]:
        for j in board[i]:
            gcnt[j]-=1
            if gcnt[j]==0:
                nex.append(j)
print(' '.join(que))