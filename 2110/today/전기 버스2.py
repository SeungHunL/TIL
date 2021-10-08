def dp(s):
    ans[s]=-1
    for i in range(N-1):
        for j in range(1,charge[i]+1):
            if i+j<N and ans[i+j]>ans[i]+1:
                ans[i+j]=ans[i]+1


for q in range(int(input())):
    com = list(map(int, input().split()))
    N=com[0]
    charge=com[1:]
    ans = [10000] * N
    dp(0)
    print(f'#{q + 1} {ans[-1]}')
