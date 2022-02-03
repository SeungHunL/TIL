def find(parent,x):
    if parent[x]==x:
        return x
    parent[x]=find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    rootA=find(parent,a)
    rootB=find(parent,b)

    if rootA<rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

def solution(n, costs):
    answer = 0

    costs.sort(key=lambda x : x[2])

    parent=[0]*(n+1)
    for i in range(n+1):
        parent[i]=i

    for edge in costs:
        a,b,cost=edge

        if find(parent,a) !=find(parent,b):
            union(parent,a,b)
            answer+=cost
    return answer

print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))