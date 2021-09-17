import sys

input = sys.stdin.readline


class Node:
    def __init__(self, data,left_node,right_node):
        self.data = data
        self.left = left_node
        self.right = right_node


def preorder(node):
    print(node.data, end='')
    if node.left != None:
        preorder(tree[node.left])
    if node.right != None:
        preorder(tree[node.right])

def inorder(node):
    if node.left != None:
        inorder(tree[node.left])
    print(node.data, end='')
    if node.right != None:
        inorder(tree[node.right])

def postorder(node):
    if node.left != None:
        postorder(tree[node.left])
    if node.right != None:
        postorder(tree[node.right])
    print(node.data, end='')


N = int(input())
tree = {}

for _ in range(N):
    a, b, c = input().split()
    if b=='.':
        b=None
    if c=='.':
        c=None
    tree[a] = Node(a, b, c)
preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])