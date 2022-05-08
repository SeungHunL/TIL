import sys

input = sys.stdin.readline

N = int(input())
start_blocks = [list(map(int, input().split())) for _ in range(N)]
ans = 0


def moveBlock(blocks, d, c):
    global ans
    nblocks = [[0] * N for _ in range(N)]
    if d == 0:
        for i in range(N):
            s = 0
            block = []
            for j in range(1, N + 1):
                if blocks[i][-j]:
                    if s:
                        if blocks[i][-j] == s:
                            block.append(2 * s)
                            s = 0
                        else:
                            block.append(s)
                            s = blocks[i][-j]
                    else:
                        s = blocks[i][-j]
            else:
                if s:
                    block.append(s)
                block += [0] * (N - len(block))
            blocks[i] = block[::-1]
    elif d == 1:
        for i in range(N):
            s = 0
            block = []
            for j in range(N):
                if blocks[i][j]:
                    if s:
                        if blocks[i][j] == s:
                            block.append(2 * s)
                            s = 0
                        else:
                            block.append(s)
                            s = blocks[i][j]
                    else:
                        s = blocks[i][j]
            else:
                if s:
                    block.append(s)
                block += [0] * (N - len(block))
            blocks[i] = block
    elif d == 2:
        for i in range(N):
            s = 0
            block = []
            for j in range(N):
                if blocks[j][i]:
                    if s:
                        if blocks[j][i] == s:
                            block.append(2 * s)
                            s = 0
                        else:
                            block.append(s)
                            s = blocks[j][i]
                    else:
                        s = blocks[j][i]
            else:
                if s:
                    block.append(s)
                block += [0] * (N - len(block))
            for k in range(N):
                nblocks[k][i] = block[k]
        blocks = nblocks
    else:
        for i in range(1, N + 1):
            s = 0
            block = []
            for j in range(1, N + 1):
                if blocks[-j][-i]:
                    if s:
                        if blocks[-j][-i] == s:
                            block.append(2 * s)
                            s = 0
                        else:
                            block.append(s)
                            s = blocks[-j][-i]
                    else:
                        s = blocks[-j][-i]
            else:
                if s:
                    block.append(s)
                block += [0] * (N - len(block))
            for k in range(1, N + 1):
                nblocks[-k][-i] = block[k - 1]
        blocks = nblocks
    if c == 4:
        for block in blocks:
            ans = max(ans, max(block))
        return
    for l in range(4):
        moveBlock(blocks[::], l, c + 1)


for u in range(4):
    moveBlock(start_blocks[::], u, 0)
print(ans)
