import sys


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def push(self,value):
        node = Node(data=value)
        tempNode = self.root

        if self.root is None:
            self.root = node
            return


N, M, K = map(int, sys.stdin.readline().split())
numl = []
for _ in range(N):
    numl.append(int(sys.stdin.readline()))

root=Node(sum(numl))
root.left=sum(numl)



for _ in range(M + K):
    ans = 0
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        numl[b - 1] = c
    else:
        for i in range(b - 1, c):
            ans += numl[i]
        print(ans)
