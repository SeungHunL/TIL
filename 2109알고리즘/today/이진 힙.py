
class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


class Tree:
    def __init__(self):
        self.root = None

    def push(self, n):
        if self.root == None:
            self.root = Node(n)
            return
        que = []
        que.append(self.root)
        while que:
            s = que.pop(0)
            if not s.left:
                s.left = Node(n, s)
                p = s.left
                break
            elif not s.right:
                s.right = Node(n, s)
                p = s.right
                break
            que.append(s.left)
            que.append(s.right)

        global total
        total = 0
        q=p
        while p.data < p.parent.data:
            p.data, p.parent.data = p.parent.data, p.data
            p = p.parent
            if p.parent == None:
                break

        while 1:
            if q.parent == None:
                break
            total += q.parent.data
            q = q.parent
T = int(input())

for _ in range(T):
    N = int(input())
    nl = list(map(int, input().split()))
    bintree = Tree()
    total = 0
    for i in nl:
        bintree.push(i)

    print(f'#{_ + 1} {total}')
