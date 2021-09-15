import sys
from collections import deque


def bfs(arr, n):
    # 테두리 두르기
    ar = [[0] * (n + 2)]
    for l in range(n):
        ar.append([0] + arr[l] + [0])
    ar.append([0] * (n + 2))
    # 델타 사용
    count = []
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    deq = deque()
    # deque queue 에서 .pop(0)를 하는 것보다 시간 복잡도 개선
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # 무리 찾기
            if ar[i][j] == 1:
                deq.append((i, j))
                cnt = 0
                # 무리가 전부 0이 될 때까지
                while deq:
                    q = deq.popleft()
                    ar[q[0]][q[1]] = 0
                    cnt += 1
                    for m in range(4):
                        # 사방에 1인 값이 있으면 데크에 추가, 데크에 없을 때
                        if ar[q[0] + dy[m]][q[1] + dx[m]] == 1 and (q[0] + dy[m], q[1] + dx[m]) not in deq:
                            deq.append((q[0] + dy[m], q[1] + dx[m]))
                count.append(cnt)
    count.sort()
    print(len(count))
    for __ in count:
        print(__)
    return


N = int(sys.stdin.readline())
maps = []
for _ in range(N):
    maps.append(list(map(int, list(sys.stdin.readline().strip()))))
bfs(maps, N)
