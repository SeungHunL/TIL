from collections import deque

T = int(input())


def bfs(arr, s):
    que=deque()
    for z in s:
        que.append(z)

    while que:
        ty, tx = que.popleft()
        c = arr[ty][tx]
        for r in range(4):
            ry = ty+ dy[r]
            rx = tx+dx[r]
            if 0 <= rx < M and 0 <= ry < N and arr[ry][rx]>c+1:
                arr[ry][rx] = c + 1
                que.append((ry, rx))


for _ in range(T):
    N, M = map(int, input().split())
    dx = (1, 0, -1, 0)
    dy = (0, -1, 0, 1)
    INF = int(1e9)
    string = []
    wat = []
    for n in range(N):
        a = input()
        b = []
        for i in range(M):
            if a[i] == 'W':
                wat.append((n, i))
                b.append(0)
            else:
                b.append(INF)
        string.append(b)

    bfs(string, wat)

    total = 0
    for q in range(N):
        for p in range(M):
            total += string[q][p]

    print(f'#{_ + 1} {total}')
