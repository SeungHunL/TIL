def dfs(n,t=0,percent=1):
    global ans,use
    # 방문 처리
    use+=[n]
    percent*=com[t][n]*0.01
    t+=1

    # 종료 조건
    if t==N:
        if percent>ans:
            ans=percent
        return
    # 후보 제거
    if percent<=ans:
        return
    for i in range(N):
        if i not in use:
            dfs(i,t,percent)
            use=use[:t]

for q in range(int(input())):
    N = int(input())
    com=[]
    for i in range(N):
        com.append(list(map(int, input().split())))
    ans=0
    for j in range(N):
        use=[]
        dfs(j)
    print(f'#{q + 1} {ans*100:6f}')