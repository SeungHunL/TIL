def prim(start):
    global ans
    check = [0] * N
    table = [0] * N
    check[start] = 1
    table[start] = 0
    cnt=0
    for i in range(N):
        if adj[start][i]:
            table[i] = adj[start][i]
    while 1:
        if cnt==N-1:
            break
        cnt+=1
        mn=100000000000
        for i in range(N):
            if not check[i]:
                if table[i]<mn:
                    idx = i
                    mn=table[i]
        ans+=(table[idx])**2
        check[idx] = 1
        for i in range(N):
            if 0< adj[idx][i] < table[i]:
                table[i] = adj[idx][i]

for q in range(int(input())):
    N =int(input())
    point=[]
    for e in range(2):
        point.append(list(map(int, input().split())))
    E=float(input())
    adj=[[0]*N for a in range(N)]
    for i in range(N):
        x1=point[0][i]
        y1=point[1][i]
        for j in range(i+1,N):
            adj[i][j]=adj[j][i]=((x1-point[0][j])**2+(y1-point[1][j])**2)**0.5
    ans=0

    prim(0)

    ans*=E
    if (ans%1)<0.5:
        ans=int(ans)
    else:
        ans=int(ans)+1
    print(f'#{q + 1} {ans}')