def move(y, x, s):
    global ans
    if s == 3 and (y==i and x==j):
        if len(visit) > ans:
            ans = len(visit)
        return
    elif not 0<=y<N or not 0<=x<N:
        return
    elif cafe[y][x] in visit:
        return
    else:
        visit.append(cafe[y][x])
        for o in [0,1]: # 0은 정방향 1은 왼쪽
            s+=o
            if s>3:
                break
            move(y + d[s][0], x + d[s][1], s)
        else:
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
                move(i, j, 0)
    print(f'#{q + 1} {ans}')
