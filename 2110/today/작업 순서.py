from collections import deque

for q in range(10):
    V, E = map(int, input().split())
    tlist = list(map(int, input().split()))
    cond = [0] * (V + 1)  # 진입차수
    adj = [[] for i in range(V + 1)]
    for i in range(E):
        adj[tlist[2 * i]] += [tlist[2 * i + 1]]
        cond[tlist[2 * i + 1]] += 1

    que = deque()
    check = [0] * (V + 1)
    for j in range(1, V + 1):
        if not cond[j]:
            check[j] = 1
            que.append(j)
    ans = []
    while que:
        a = que.popleft()
        ans.append(f'{a}')
        for b in adj[a]:
            cond[b] -= 1
        for j in range(1, V + 1):
            if not check[j] and not cond[j]:
                check[j] = 1
                que.append(j)

    ans = ' '.join(ans)
    print(f'#{q + 1} {ans}')
