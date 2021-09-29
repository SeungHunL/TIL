from collections import deque

def bfs(arr, s,time):
    que=deque()
    que.append(s)
    sque=deque()
    cnt=0
    if time ==1:
        return 1
    while time:
        if len(que)==0:
            for i in sque:
                que.append(i)
            time-=1
        ty, tx = que.popleft()

        k = arr[ty][tx]
        arr[ty][tx] = 0

        if k==0:
            continue
        cnt += 1
        for r in pipe[k]:
            ry = ty+ r[0]
            rx = tx+ r[1]
            if 0 <= rx < M and 0 <= ry < N:
                e =arr[ry][rx]
                if e!=0 and (-r[0],-r[1]) in pipe[e] :
                    sque.append((ry, rx))
    return cnt


T = int(input())

dx = (1, 0, -1, 0)
dy = (0, -1, 0, 1)
pipe = {
    1: [(1, 0), (0, 1), (-1, 0), (0, -1)],
    2: [(1, 0), (-1, 0)],
    3: [(0, 1), (0, -1)],
    4: [(-1, 0), (0, 1)],
    5: [(1, 0), (0, 1)],
    6: [(1, 0), (0, -1)],
    7: [(-1, 0), (0, -1)],
}
for _ in range(T):
    N, M, R, C, L = map(int, input().split())
    maps = []
    for __ in range(N):
        maps.append(list(map(int, input().split())))
    s = (R, C)
    ans = bfs(maps, s, L)
    print(f'#{_ + 1} {ans}')
