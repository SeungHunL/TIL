import sys
input=sys.stdin.readline
str1=input().strip().upper()
str2=input().strip().upper()
l1=len(str1)
l2=len(str2)
ans=[[0]*l2 for i in range(l1)]
for i in range(l1):
    for j in range(l2):
        if i==0:
            if str1[i] in str2[:j+1]:
                ans[i][j]=1
        elif j==0:
            if str2[j] in str1[:i+1]:
                ans[i][j]=1
        elif str1[i]==str2[j]:
            if max(ans[i-1][j],ans[i][j-1])<= min(i,j):
                ans[i][j] = max(ans[i - 1][j], ans[i][j - 1])+1
            else:
                ans[i][j]= max(ans[i-1][j],ans[i][j-1])
        elif str1[i]!=str2[j]:
            ans[i][j] = max(ans[i - 1][j], ans[i][j - 1])
print(ans[-1][-1])


