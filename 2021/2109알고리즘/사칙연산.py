

class Node:
    def __init__(self,data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def cal(node):
    if type(Tree[node.left].data) != int:
        cal(Tree[node.left])
    if type(Tree[node.right].data) != int:
        cal(Tree[node.right])
    a = Tree[node.left].data
    b = Tree[node.right].data
    if node.data == '/':
        node.data = a / b
    elif node.data == '*':
        node.data = a * b
    elif node.data == '+':
        node.data = a + b
    elif node.data == '-':
        node.data = a - b


for _ in range(10):
    N = int(input())

    Tree={}
    for __ in range(N):
        a = list(input().split())
        if len(a)==4:
            Tree[int(a[0])]=Node(a[1],int(a[2]),int(a[3]))
        else:
            Tree[int(a[0])]=Node(int(a[1]))
    cal(Tree[1])

    print(f'#{_ + 1} {int(Tree[1].data)}')
