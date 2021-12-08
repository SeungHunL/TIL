def dfs(start):
    global ans,use
    # 방문 처리
    use.append(start)
    l=len(use)
    # 종료 조건
    if l==N:
        ans+=1
        return
    # 후보 제거

    for i in range(N):
        if i not in use:
            for j in range(1,l+1):
                if abs(use[-j]-i)==j:
                    break
            else:
                dfs(i)
                use=use[:l]


for q in range(int(input())):
    N=int(input())
    ans=0
    for i in range(N):
        use=[]
        dfs(i)
    print(f'#{q + 1} {ans}')