import sys

input = sys.stdin.readline


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def solution(start, end):
    if end - start == 2:
        tree[b[start + 1]] = Node(b[start + 1], b[start], b[end])
        return b[start + 1]
    div = (start + end) // 2
    tree[b[div]] = Node(b[div], solution(start, div - 1), solution(div + 1, end))
    return b[div]


K = int(input())
b = list(map(int, input().split()))
tree = {}
ans = [[] for _ in range(K)]

solution(0, len(b) - 1)

start = b[len(b) // 2]
que = [start]
for i in range(K):
    for k in que:
        ans[i].append(k)
    que = []
    if i == K - 1:
        break
    for j in ans[i]:
        que.append(tree[j].left)
        que.append(tree[j].right)
for i in ans:
    for j in i:
        print(j, end=' ')
    print()
