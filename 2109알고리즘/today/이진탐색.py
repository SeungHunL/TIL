T= int(input())


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def inorder(node):
    global cnt
    if node.left in Tree:
        inorder(Tree[node.left])
    node.data = cnt
    cnt += 1
    if node.right in Tree:
        inorder(Tree[node.right])


def maketree(n, Tree):
    for i in range(1, n + 1):
        Tree[i] = Node(i, 2 * i, 2 * i + 1)


for _ in range(T):
    N = int(input())
    Tree = {}
    cnt = 1
    maketree(N, Tree)
    inorder(Tree[1])

    print(f'#{_ + 1} {Tree[1].data} {Tree[N // 2].data}')
