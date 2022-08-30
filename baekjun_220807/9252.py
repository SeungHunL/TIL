import sys

input = sys.stdin.readline

a=input().strip()
b=input().strip()
dp2=[['']*(len(b)+1) for i in range(len(a)+1)]
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            dp2[i+1][j+1]=dp2[i][j]+a[i]
        else:
            if len(dp2[i][j+1])>len(dp2[i+1][j]):
                dp2[i+1][j+1]=dp2[i][j+1]
            else:
                dp2[i+1][j+1]=dp2[i+1][j]
print(len(dp2[-1][-1]))
print(dp2[-1][-1])
