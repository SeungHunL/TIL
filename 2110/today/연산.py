from collections import deque


def bfs(n):
    que = deque()
    que.append(n)

    l = 1
    c = 1
    while que:
        t = que.popleft()

        tape = [t - 1, t + 1, t * 2, t - 10]
        for i in tape:
            if 0 <= i < 2 * M and not done[i]:
                if i == M:
                    return c
                que.append(i)
                done[i]=1
        l -= 1
        if not l:
            l = len(que)
            c += 1


for q in range(int(input())):
    N, M = map(int, input().split())
    done = [0] * 2 * M
    print(f'#{q + 1} {bfs(N)}')