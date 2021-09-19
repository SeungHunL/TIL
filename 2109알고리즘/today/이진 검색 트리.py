import sys

input = sys.stdin.readline


class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def postorder(node):
    if node.left != None:
        postorder(tree[node].left)
    if node.right != None:
        postorder(tree[node].right)
    print(node.data, end='')


start = int(input())

tree = {}

nlist = [start]
while True:
    try:
        nlist.append(int(input()))
        if nlist[-1] < nlist[-2]:
            tree[nlist[-2]] = Node(nlist[-2], nlist[-1])
            tree[nlist[-1]] = Node(None)
        else:
            if not tree[start].right and nlist[-1] > start:
                tree[start].right = nlist[-1]
            if nlist[-2] < nlist[-1] < nlist[-3]:
                tree[nlist[-2]].right = nlist[-1]
    except:
        break
postorder(tree[start])