import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

LCS = [[0]*len(str2) for _ in range(len(str1))]
for i in range(len(str1)):
    for j in range(len(str2)):
        if i == 0 or j == 0:  # 마진 설정
            if str1[i] == str2[j]:
                LCS[i][j] = 1
            else:
                LCS[i][j] = 0
        elif str1[i] == str2[j]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:
            LCS[i][j] = 0
ans = 0
for s in LCS:
    if ans<max(s):
        ans=max(s)
print(ans)