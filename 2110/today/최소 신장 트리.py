def prim(start):
    global ans
    check[start] = 1
    table[start] = 0
    cnt=0
    for i in range(V + 1):
        if adj[start][i]:
            table[i] = adj[start][i]
    while 1:
        if cnt==V:
            break
        cnt+=1
        mn=10000
        for i in range(V+1):
            if not check[i]:
                if table[i]<mn:
                    idx = i
                    mn=table[i]
        ans+=table[idx]
        check[idx] = 1
        for i in range(V + 1):
            if 0< adj[idx][i] < table[i]:
                table[i] = adj[idx][i]


for q in range(int(input())):
    V, E = map(int, input().split())
    adj = [[0] * (V + 1) for a in range(V + 1)]
    for e in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1][n2] = adj[n2][n1] = w
    check = [0] * (V + 1)
    table = [10000] * (V + 1)
    ans = 0
    prim(0)
    print(f'#{q + 1} {ans}')
