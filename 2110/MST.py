def MST(start):
    visit=[]
    cand={}
    for i in range(N):
        cand.append(adj[start])

N=6
M=10
adj=[]
for i in range(M):
    adj.append(list(map(int,input().split())))

# 인접 행렬
adj=[[0]*(V+1)for a in range(V+1)]
for e in range(E):
    n1,n2,w=map(int,input().split())
    adj[n1][n2]=adj[n2][n1]=w
for d in adj:
    print(d)

# adj={}
    # wlist=[]
    # for e in range(E):
    #     n1,n2,w=map(int,input().split())
    #     if w in adj:
    #         adj[w]=adj[w]+[(n1,n2)]
    #     else:
    #         adj[w]=[(n1,n2)]
    #     wlist.append(w)