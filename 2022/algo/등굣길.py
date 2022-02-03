from collections import deque
def solution(m, n, puddles):
    maps = [[0] * m for _ in range(n)]
    maps[0][0]=1
    for p in puddles:
        maps[p[1] - 1][p[0] - 1] = -1
    d = [[1, 0], [0, 1]]
    arr = deque([(0, 0)])
    nex = []
    while arr:
        y, x = arr.popleft()
        for dy, dx in d:
            ty = y + dy
            tx = x + dx
            if 0 <= ty <= n - 1 and 0 <= tx <= m - 1 and maps[ty][tx] != -1:
                maps[ty][tx] += maps[y][x]
                nex.append((ty,tx))
        if not arr and nex:
            print(maps)
            arr=deque(list(set(nex)))
            nex=[]
            print(arr)
    return maps[-1][-1]%1000000007

# solution(4,3,[[2,2]])
solution(4,3,[[2,2]])