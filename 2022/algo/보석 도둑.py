import sys
import heapq

input = sys.stdin.readline
N, K = map(int, input().split())
jewels=[]
bags = []
que = []
for _ in range(N):
    jewels.append(list(map(int, input().split())))
for _ in range(K):
    bags.append(int(input()))
jewels.sort()
bags.sort()
ans = 0
for bag in bags:
    while jewels and bag >= jewels[0][0]:
        heapq.heappush(que, -jewels[0][1])  # Max heap
        heapq.heappop(jewels)
    if que:
        ans += heapq.heappop(que)
    elif not jewels:
        break
print(-ans)
