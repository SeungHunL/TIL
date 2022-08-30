import sys

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

input = sys.stdin.readline


N = int(input())
nums=list(map(int,input().split()))
t = int(input())

dic={}
for i in range(N):
    if nums[i]==-1:
        # root=Node(i)
        root=i
        if i not in dic:
            dic[i]=[]
    else:
        r=nums[i]
        if r in dic:
            dic[r].append(i)
        else:
            dic[r]=[i]
if root==t:
    print(0)
else:
    # print(dic)
    que=[root]
    c=0
    while que:
        s=que.pop()
        if s in dic:
            if t in dic[s]:
                dic[s].remove(t)
            if dic[s]:
                que+=dic[s]
            else:
                c+=1
        else:
            c+=1

    print(c)