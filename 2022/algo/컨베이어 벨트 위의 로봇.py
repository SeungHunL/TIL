import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())
belts = deque(list(map(int, input().split())))
robots = deque([False] * N)
take = 0
while True:
    # 1
    robots.rotate(1)
    belts.rotate(1)
    # 2
    robots[N - 1] = False
    for i in range(N - 2, -1, -1):
        if robots[i]:
            if not robots[i + 1] and belts[i + 1]:
                robots[i] = False
                belts[i + 1] -= 1
                if i + 1 != N - 1:
                    robots[i + 1] = True
    # 3
    if belts[0]:
        robots[0] = True
        belts[0] -= 1
    take += 1
    # 4
    if belts.count(0) >= K:
        break
print(take)
