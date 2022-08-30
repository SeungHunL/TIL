import sys

input = sys.stdin.readline
N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs(y, x, v):
    global ans,c
    for d in dir:
        ty, tx = y + d[0], x + d[1]
        if 0 <= ty < N and 0 <= tx < M:
            n = ord(board[ty][tx]) - 65
            if v[n] == 0:
                v[n] = 1
                c+=1
                ans = max(ans, c)
                dfs(ty, tx, v[:])
                v[n] = 0
                c-=1


ans = 1
c=1
vis=[0] * 26
vis[ord(board[0][0]) - 65]=1
dfs(0, 0, vis[:])
print(ans)