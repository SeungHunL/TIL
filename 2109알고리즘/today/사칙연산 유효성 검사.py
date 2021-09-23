

class Node:
    def __init__(self,data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def cal(ts):
    if ts.left.isdigit() and ts.right.isdigit():
        if ts.data=='/':
            return ts.left/ts.right
        if ts.data=='*':
            return ts.left*ts.right
        if ts.data=='+':
            return ts.left+ts.right
        if ts.data=='-':
            return ts.left-ts.right
    else:
        return int(ts.data)


for _ in range(10):
    N = int(input())
    flag=0

    Tree={}
    for __ in range(N):
        a = list(input().split())
        if len(a)==4:
            Tree[a[0]]=Node(a[1],a[2],a[3])
        elif len(a)==2:
            Tree[a[0]]=Node(a[1])
        else:
            flag=1

    if flag:
        print(f'#{_+1} 0')
    else:
        print(cal(Tree['1']))
        print(f'#{_ + 1} 1')
