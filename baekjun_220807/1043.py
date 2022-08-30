import sys

input = sys.stdin.readline

N,M = map(int,input().split())
know=list(map(int,input().split()))
graph=[0]*(N+1)
for i in know:
    if i==0:
        pass
    else:
        graph[i]=1

ans=0
for i in range(M):
    party=list(map(int,input().split()))[1:]
    for j in party:
        if graph[j]:
            break
    else:
        ans+=1
print(ans)