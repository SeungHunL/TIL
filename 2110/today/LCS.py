import sys

input = sys.stdin.readline
str1 = input().strip().upper()
str2 = input().strip().upper()
l1 = len(str1)
l2 = len(str2)
ans = [[0] * (l2 + 1) for i in range(l1 + 1)]
for i in range(1, l1 + 1):
    for j in range(1, l2 + 1):
        if str1[i - 1] == str2[j - 1]:
            ans[i][j] = ans[i - 1][j-1] + 1
        else:
            ans[i][j] = max(ans[i - 1][j], ans[i][j - 1])
print(ans[-1][-1])
