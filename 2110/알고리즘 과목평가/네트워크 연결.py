import sys

def cycle(start,end):
    stack=[]
    stack.append(start)
    visit=[0]*N
    while stack:
        k =stack.pop()
        visit[k]=1
        if k==end:
            return False
        for i in ans[k]:
            if not visit[i]:
                stack.append(i)
    return True

def krus(arr):
    total=0
    cnt=0
    for i in range(len(arr)):
        if cnt==N-1:
            break
        start,end,value=arr[i]
        if start in ans and end in ans:
            if cycle(start,end):
                cnt+=1
                total+=value
                ans[start] = ans[start] + [end]
                ans[end] = ans[end] + [start]
        else:
            if start in ans:
                ans[start]=ans[start]+[end]
                ans[end] = [start]
            elif end in ans:
                ans[start] = [end]
                ans[end] = ans[end]+[start]
            else:
                ans[start]=[end]
                ans[end] = [start]
            cnt+=1
            total += value
    return total

input=sys.stdin.readline
N=int(input())
M=int(input())
al=[]
for i in range(M):
    al.append(list(map(int,input().split())))
al.sort(key=lambda x:x[2])
ans={}
print(krus(al))
