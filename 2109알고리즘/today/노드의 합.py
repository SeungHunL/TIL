class Node:
    def __init__(self, data,left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def suml(node):
    if Tree[node.left].data == 0:
        suml(Tree[node.left])
    if node.right in Tree and Tree[node.right].data == 0:
        suml(Tree[node.right])
    if node.right in Tree:
        node.data = Tree[node.left].data + Tree[node.right].data
    else:
        node.data = Tree[node.left].data

T = int(input())
for _ in range(T):
    N, M, L = map(int, input().split())
    Tree = {}
    for i in range(1, N + 1):
        Tree[i] = Node(0, 2 * i, 2 * i + 1)
    for __ in range(M):
        a, b = map(int, input().split())
        Tree[a].data = b
    suml(Tree[1])
    ans = Tree[L].data
    print(f'#{_ + 1} {ans}')