import sys


def go(visit, tmp, now):
    global ans
    visit[now] = True
    #종료조건
    if now == N - 1:
        if visit[now - 1] == True and visit[now - 2] == True:
            return
        ans = max(ans, tmp)
        return
    elif now > N - 1:
        return


    if now == 0:
        go(visit[:], tmp + ss[1], 1)
        go(visit[:], tmp + ss[2], 2)
    elif now == 1:
        if visit[0]==False:
            go(visit[:], tmp + ss[2], 2)
        go(visit[:], tmp + ss[3], 3)
    else:
        if visit[now - 1] == True and visit[now - 2] == True:
            return
        else:
            go(visit[:], tmp + ss[now + 1], now + 1)

        if now+2<N:
            go(visit[:], tmp + ss[now + 2], now + 2)





input = sys.stdin.readline

N = int(input())
ss = []
for i in range(N):
    ss.append(int(input()))
ans = 0
go([False] * (N + 1), ss[0], 0)
go([False] * (N + 1), ss[1], 1)
print(ans)