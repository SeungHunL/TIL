import sys

input = sys.stdin.readline

n = int(input())
triangle = []
dp = [[0] * i for i in range(1, n + 1)]
for _ in range(n):
    triangle.append(list(map(int, input().split())))

max_score = 0
dp[0][0] = triangle[0][0]
for i in range(1, n):
    for j in range(i + 1):
        if 0<j<i:
                dp[i][j] = max(dp[i - 1][j-1], dp[i - 1][j]) + triangle[i][j]
        elif j==0:
            dp[i][j] = dp[i - 1][j] + triangle[i][j]
        else:
            dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
print(max(dp[-1]))
