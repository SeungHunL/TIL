T = int(input())
for _ in range(T):
    E, N = map(int, input().split())
    Elist = list(map(int, input().split()))
    Tree = {}
    for i in range(E):
        if Elist[2 * i] in Tree:
            Tree[Elist[2 * i]] = [Elist[2 * i + 1]] + Tree[Elist[2 * i]]
        else:
            Tree[Elist[2 * i]] = [Elist[2 * i + 1]]
    que = []
    que.append(N)
    cnt = 0
    while que:
        s = que.pop()
        cnt += 1
        if s in Tree:
            que += Tree[s]

    print(f'#{_+1} {cnt}')
