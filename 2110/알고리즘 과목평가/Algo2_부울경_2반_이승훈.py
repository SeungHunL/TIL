def find(start):
    global ans
    y,x=start
    # 4방향의 델타값
    for dy,dx in d:
        ty=y+dy
        tx=x+dx
        # 미로 안의 좌표이고 방문하지 ty,tx 좌표를 방문하지 않았을 때
        if 0<=ty<N and 0<=tx<N and not visit[ty][tx]:
            # 경로가 있을 때
            if maps[ty][tx]==0:
                # 방문 표시
                visit[ty][tx]=1
                # 방문 표시를 가진 채로 재귀
                find((ty,tx))
                # 방문했다가 나와서 표시를 풀고 다음 for 문 반복
                visit[ty][tx]=0
            # 도착점까지 도달했을 때
            elif maps[ty][tx]==3:
                ans+=1
# 4방향의 델타 값
d=[(0,1),(1,0),(0,-1),(-1,0)]
for q in range(int(input())):
    N = int(input())
    # 미로 판 2차원 리스트로 입력
    maps = []
    for i in range(N):
        maps.append(list(map(int, input().split())))
    # 시작점 찾기
    for j in range(N):
        for k in range(N):
            if maps[j][k] == 2:
                s = (j, k)
                break
    # 방문했는지 확인하는 이차원 리스트
    visit = [[0] * N for w in range(N)]
    ans = 0
    find(s)
    if ans:
        # 도착점까지 도달한 횟수를 나타낸 ans 가 있을 때
        print(f'#{q + 1} 1 {ans}')
    else:
        print(f'#{q + 1} 0')
