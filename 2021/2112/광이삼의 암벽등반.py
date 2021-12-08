from collections import deque

def bfs(s):
    queue =deque(s)
    while queue:
        vy,vx=queue.popleft()
        for i in range(-L,L):
            for j in range(-L,L):
                if (i,j) == (0,0) or abs(i)+abs(j)>L:
                    pass
                value = [vy + i][vx + j]
                if value==1:
                    queue.append((vy+i,vx+j))
                elif value==3:
                    




for tc in range(int(input())):
    M, N, L = map(int, input().split())
    maps=[]
    for m in range(M):
        line=list(map(int,input().split()))
        for l in range(N):
            if line[l]==2:
                sp=(m,l)
            elif line[l]==3:
                ep=(m,l)
        maps.append(line)
    bfs(sp)
    print(sp)
    print(ep)
    ans=0
    print(f'#{tc+1} {ans}')