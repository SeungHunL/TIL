import sys
def find(x):
    if parent[x]!=x:
        return find(parent[x])
    return x

def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

input = sys.stdin.readline
v, e = map(int, input().split())
el=[(tuple(map(int,input().split()))) for _ in range(e)]
el.sort(key=lambda x:x[2])
parent=[i for i in range(v+1)]
ans=0
for i in range(e):
    a,b,c=el[i]
    if find(a)!=find(b):
        union(a,b)
        ans+=c
print(ans)