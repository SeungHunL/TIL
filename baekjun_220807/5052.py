import sys
class node:
    def __init__(self,data):
        self.data=data
        self.next={}

input = sys.stdin.readline
for _ in range(int(input())):
    tc={}
    gg=0
    for __ in range(int(input())):
        nums=input().strip().replace(' ','')
        if len(nums)>10:
            gg=1
        num=nums[0]
        flag=0
        if num in tc:
            Node = tc[num]
            if Node.next:
                pass
            else:
                gg = 1
                break
            pass
        else:
            flag=1
            tc[num]=node(num)
            Node=tc[num]
        for i in range(len(nums)):
            num=nums[i]
            if i==0:
                continue
            else:
                if num in Node.next:
                    Node = Node.next[num]
                    if Node.next:
                        pass
                    else:
                        gg=1
                        break
                else:
                    flag=1
                    Node.next[num]=node(num)
                    Node=Node.next[num]
        if flag==0:
            gg=1
    if gg:
        print("NO")
    else:
        print("YES")