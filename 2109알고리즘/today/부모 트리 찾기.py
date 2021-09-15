import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
tree = [0] * (N + 1)
check = [False] * (N + 1)
check[1] = True
que = deque()


def CheckTree(n, m):
    if check[n]:
        check[m] = True
        tree[m] = n
    elif check[m]:
        check[n] = True
        tree[n] = m
    else:
        que.append((n, m))


for _ in range(N - 1):
    a, b = map(int, input().split())
    CheckTree(a, b)

while que:
    (a, b) = que.popleft()
    CheckTree(a, b)

for k in range(2, N + 1):
    print(tree[k])
