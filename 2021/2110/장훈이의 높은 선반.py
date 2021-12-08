def comb(visit, res=0,s=0):
    global ans
    if s == N:
        if res>=B:
            if ans>res:
                ans=res
        return
    comb(visit,res,s+1)
    visit[s]=1
    comb(visit, res+nums[s], s + 1)
    visit[s]=0


for q in range(int(input())):
    N, B = map(int, input().split())
    nums = list(map(int, input().split()))
    ans = 10000000
    comb([0] * N)

    print(f'#{q + 1} {ans-B}')
