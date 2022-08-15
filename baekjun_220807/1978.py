import sys

input=sys.stdin.readline

N=int(input())
nums=list(map(int,input().split()))
deck=[2,3]
if max(nums)>3:
    for i in range(4,max(nums)+1):
        for j in deck:
            if i%j==0:
                break
        else:
            deck.append(i)
ans=0
for num in nums:
    for i in deck:
        if num<i:
            pass
        else:
            if num==i:
                ans+=1
                break
print(ans)