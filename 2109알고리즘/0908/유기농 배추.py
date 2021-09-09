import sys
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(int(sys.stdin.readline())):
    M, N, K = map(int, sys.stdin.readline().split())
    que = deque()
    stack=[]
    for k in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        stack.append((Y,X))
    cnt = 0
    while stack:
        que.append(stack[0])
        while que:
            ty, tx = que.popleft()
            stack.remove((ty,tx))
            for k in range(4):
                if (ty + dy[k],tx + dx[k]) in stack and (ty + dy[k],tx + dx[k]) not in que :
                    que.append((ty + dy[k],tx + dx[k]))
        cnt += 1
    print(cnt)