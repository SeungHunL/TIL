# for _ in range(int(input())):
#     N = int(input())
#     cube = []
#     for __ in range(N):
#         cube.append(list(map(int, input().split())))
#
#     visit=[0]*N

def DFS(v,check,N,load):
    check[v]=1
    load.append(v)
    for i in range(N):
        if not check[i]:
            DFS(i,check,N,load)


N=5
for i in range(N):
    visit = [0] * N
    path = []
    DFS(i,visit,N,path)
    print(path)
