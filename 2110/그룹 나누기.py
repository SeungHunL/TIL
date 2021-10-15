from collections import deque

def graph():
    res=[[] for j in range(N+1)]
    for i in range(M):
        res[Ms[2*i]].append(Ms[2*i+1])
        res[Ms[2 * i+1]].append(Ms[2 * i])
    return res

def bfs(start):
    que=deque()
    que.append(start)
    while que:
        t=que.popleft()
        for i in team[t]:
            if not use[i]:
                use[i]=1
                que.append(i)

for q in range(int(input())):
    N, M = map(int, input().split())
    Ms = list(map(int, input().split()))
    team=graph()
    use = [0] * (N + 1)
    ans=0
    for i in range(1,N+1):
        if not use[i]:
            if team[i]:
                bfs(i)
            ans+=1


    print(f'#{q + 1} {ans}')
