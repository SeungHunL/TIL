import sys

input = sys.stdin.readline


class Node:
    def __init__(self, data,left,right):
        self.data = data
        self.left = left
        self.right = right

def postorder(node):
    if node.left != None:
        postorder(node.left)
    if node.right != None:
        postorder(node.right)
    print(node.data)


tree = {}
N = []
N.append(int(input()))

while N:
    N.append(int(input()))
    d=N[-4]
    a=N[-3]
    b=N[-2]
    c=N[-1]
    if c < b:
        if c < a:
            continue

    elif c > b:
        if c > a and c<d:
            tree[a]=Node(a,b,c)
        else:
            tree[b]=Node(b,None,c)
    else:



    if len(N)==1 and N[0] in tree:
        break

postorder(tree[s])