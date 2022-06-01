import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [1]
for i in range(1, n):
    t = 0
    for j in range(i):
        if nums[j] < nums[i] and t < dp[j]:
            t = dp[j]
    dp.append(t + 1)
print(max(dp))