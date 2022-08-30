import sys

def bs(num):
    s=1
    e=len(ans)-1
    while s<=e:
        m=(s+e)//2
        if ans[m] == num:
            return m
        elif ans[m] < num:
            s=m+1
        else:
            e=m-1
    return s

input = sys.stdin.readline


N = int(input())
nums=list(map(int,input().split()))
ans=[0]
for num in nums:
    if ans[-1]<num:
        ans.append(num)
    else:
        ans[bs(num)]=num
print(len(ans)-1)