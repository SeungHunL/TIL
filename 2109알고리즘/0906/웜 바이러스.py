import sys


def dfs(arr,s,v):
    if s!=1:
        v[s]=1
    for i in arr[s]:
        if not v[i]:
            dfs(arr,i,v)
    return


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
visited=[0]*(N+1)
num_d = [[] for __ in range(N+1)]
for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    num_d[start].append(end)
    num_d[end].append(start)
dfs(num_d,1,visited)
print(visited.count(1))