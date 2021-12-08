def select(res):
    global ans
    use = [0] * N
    for r in res:
        use[((N - 1) if r-1<0 else r-1)] = 1
        use[r] = 1
        use[(0 if r+1>=N else r+1)] = 1
    if len(res) == 4:
        total = (sub[res[0]] + sub[res[1]]) ** 2 + (sub[res[2]] + sub[res[3]]) ** 2
        if total > ans:
            if res[0] < res[1] < res[2] < res[3] or res[1] < res[2] < res[3] < res[0] or res[2] < res[3] < res[0] < res[1] or res[3] < res[0] < res[1] < res[2]:
                ans = total
        return
    for i in range(N):
        if not use[i]:
            res.append(i)
            select(res)
            res.pop()


for q in range(int(input())):
    N = int(input())
    sub = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        select([i])
    print(f'#{q + 1} {ans}')
