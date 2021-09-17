import sys

input = sys.stdin.readline


class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def postorder(treedic,key):
    if not treedic[key][0]:
        postorder(treedic, treedic[key][0])
    if not treedic[key][1]:
        postorder(treedic, treedic[key][1])
    print(key)


tree = {}
N = []
start = int(input())
N.append(start)
tree[start] = [0, 0]
while N:
    N.append(int(input()))
    if N[-1] > N[-2]:
        i = 2
        while 1:
            
            if N[-i - 1] > N[-1] > N[-i]:
                tree[N[-i]][1] = N[-1]
                tree[N[-1]]=[0,0]
                break
            else:
                i+=1
    else:
        tree[N[-2]][0] = N[-1]
        tree[N[-1]] = [0,0]
    print(tree)

postorder(tree,start)