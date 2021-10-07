def dfs(n,t=0,cost=0):
    global ans,use
    # 방문 처리
    use+=[n]
    cost+=com[t][n]
    t+=1

    # 종료 조건
    if t==N:
        if cost<ans:
            ans=cost
        return
    # 후보 제거
    if cost>=ans:
        return
    for i in range(N):
        if i not in use:
            dfs(i,t,cost)
            use=use[:t]


for q in range(int(input())):
    N = int(input())
    com=[]
    for i in range(N):
        com.append(list(map(int, input().split())))
    ans=10000
    for j in range(N):
        use=[]
        dfs(j)
    print(f'#{q + 1} {ans}')