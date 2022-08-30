import sys

input = sys.stdin.readline
N=int(input())

nums = list(map(int, input().split()))
nn=[min(nums[j],nums[-j-1]) for j in range(3)]
cnt=[min(nn),sum(nn)-max(nn),sum(nn)]

ans=0
if N==1:
    ans=sum(nums)-max(nums)
else:
    c=[(N-2)*(5*N-6),8*N-12,4]
    for i in range(3):
        ans+=c[i]*cnt[i]
print(ans)
