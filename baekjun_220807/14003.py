import sys


def find(x):
    s, e = 0, len(ans) - 1
    while s <= e:
        m = (s + e) // 2
        if ans[m] == x:
            return m
        elif ans[m] > x:
            e = m - 1
        else:
            s = m + 1
    return s


input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

ans = [-2e9]
dp=[0]*(N+1)
for i in range(N):
    n=nums[i]
    if n > ans[-1]:
        ans.append(n)
        dp[i]=len(ans)-1
    else:
        fi=find(n)
        ans[fi] = n
        dp[i]=fi
print(len(ans) - 1)
c=max(dp)+1
res=[]
for i in range(N,-1,-1):
    if dp[i]==c-1:
        res.append(nums[i])
        c=dp[i]
print(*res[::-1])