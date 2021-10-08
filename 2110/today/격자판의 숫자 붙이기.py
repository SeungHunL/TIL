def dfs(y,x,res=''):
    # 종료 조건
    if len(res)==7:
        ans.add(res)
        return
    res+=f'{maps[y][x]}'
    # 후보 제거
    for i in range(4):
        ry = y + dy[i]
        rx = x + dx[i]
        if 0 <= ry < 4 and 0 <= rx < 4:
            dfs(ry,rx,res)

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
for q in range(int(input())):
    maps = []
    ans = set()
    for i in range(4):
        maps.append(list(map(int, input().split())))
    for j in range(4):
        for k in range(4):
            dfs(j, k)
    print(f'#{q + 1} {len(ans)}')
