import sys
input = sys.stdin.readline
for i in range(int(input())):
    file_count = int(input())
    files= list(map(int,input().split()))
    dp = [[1e9] * (file_count + 1) for _ in range(file_count + 1)]
    sums=[0]

    for i in range(file_count):
        sums.append(sums[-1]+files[i])
    for i in range(file_count):
        dp[i][0]=0
        dp[i][1]=files[i]
    for i in range(file_count-1):
        dp[i][2]=files[i]+files[i+1]
    for i in range(3,file_count+1): #크기
        for j in range(file_count): #시작
            if i+j<file_count+1:
                for k in range(j, j+i): # 분기점
                    print(j,k,j+i-1)
                    a=dp[j][k]+dp[k][i-k]+sums[j+i]-sums[j]
                    if a<dp[j][i]:
                        dp[j][i]=a
    for i in dp:
        print(i)
    print(dp[0][file_count])

