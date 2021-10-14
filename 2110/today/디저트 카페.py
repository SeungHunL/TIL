def move(y, x, s):
    global ans
    if s == 3 and (y==i and x==j):
        if len(visit) > ans:
            ans = len(visit)
        return
    elif not 0<=y<N or not 0<=x<N:
        return
    elif y<i:
        return
    elif cafe[y][x] in visit:
        return
    elif flag[s]and flag[s+1]:
        return
    elif s>0 and flag[s]and not flag[s-1]:
        return
    else:
        this=0
        if not flag[s]:
            flag[s]=1
            this=1
        visit.append(cafe[y][x])
        for o in [0,1]: # 0은 정방향 1은 왼쪽
            s+=o
            if s>3:
                continue
            move(y + d[s][0], x + d[s][1], s)
        else:
            if this:
                flag[s-1]=0
            visit.pop()

d = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
for q in range(int(input())):
    N = int(input())
    cafe = []
    for h in range(N):
        cafe.append(list(map(int, input().split())))
    ans=-1
    for i in range(N):
        for j in range(N):
            if (i, j) not in [(0, 0), (N - 1, 0), (0, N - 1), (N - 1, N - 1)]:
                visit=[]
                flag=[0,0,0,0,0]
                move(i, j, 0)
    print(f'#{q + 1} {ans}')
