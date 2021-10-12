from collections import deque


def oall(t=0, order=[]):
    global ans, copy
    cnt = 0
    if t == N:
        copy = [item[:] for item in block]
        for k in order:
            din(k)
        for i in range(H):
            for j in range(W):
                if copy[i][j] != 0:
                    cnt += 1
        if cnt < ans:
            ans = cnt
        return
    for i in range(W):
        order.append(i)
        oall(t + 1, order)
        order.pop()


def din(x):
    global copy
    for i in range(H):
        if copy[i][x] != 0:
            y = i
            break
    else:
        return
    boom(y, x)
    for j in range(W):
        for i in range(H - 1, -1, -1):
            e = copy[i][j]
            if e:
                copy[i][j] = 0
                while 1:
                    if i + 1 == H or copy[i + 1][j]:
                        copy[i][j] = e
                        break
                    i += 1


def boom(sy, sx):
    global copy
    que = deque()
    que.append((sy, sx))
    while que:
        ry, rx = que.popleft()
        for i in range(copy[ry][rx]):
            for j in range(1, i + 1):
                for ty, tx in [(ry - j, rx), (ry, rx - j), (ry + j, rx), (ry, rx + j)]:
                    if 0 <= ty < H and 0 <= tx < W:
                        if copy[ty][tx] <= 1:
                            copy[ty][tx] = 0
                        else:
                            que.append((ty, tx))
        copy[ry][rx] = 0
    return


for q in range(int(input())):
    N, W, H = map(int, input().split())
    block = []
    for h in range(H):
        block.append(list(map(int, input().split())))
    ans = 10000000
    oall()
    print(f'#{q + 1} {ans}')
