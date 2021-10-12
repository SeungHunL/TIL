def comb(res=[], s=0):
    if len(res) >= N // 2:
        dish(res)
        return
    if s < N:
        res.append(s)
        comb(res, s + 1)
        res.pop()
        comb(res, s + 1)


def dish(arr):
    global ans
    arr2 = []
    score1 = 0
    score2 = 0
    n = N // 2
    for i in range(n):
        for j in range(i + 1, n):
            if i != j:
                score1 += food[arr[i]][arr[j]]
    for k in range(N):
        if k not in arr:
            arr2.append(k)
    for l in range(n):
        for m in range(l + 1, n):
            if l != m:
                score2 += food[arr2[l]][arr2[m]]
    if abs(score2 - score1) < ans:
        ans = abs(score2 - score1)


for q in range(int(input())):
    N = int(input())
    ans = 10000
    food = []
    for h in range(N):
        food.append(list(map(int, input().split())))
    for i in range(N):
        for j in range(i + 1, N):
            r = food[i][j] + food[j][i]
            food[i][j], food[j][i] = r, r
    comb()

    print(f'#{q + 1} {ans}')
