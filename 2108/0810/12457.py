N = int(input())
for num in range(N):
    C = [0]*10
    A = list(map(int,list(input().strip())))
    t=r=0
    for i in A:
        C[i] += 1
    for i in range(10):
        while C[i]>=3:
            t+=1
            C[i]-=3
        while i>0and C[i-1]>=1 and C[i]>=1 and C[i+1]>=1:
            r+=1
            C[i-1]-=1
            C[i]-=1
            C[i+1]-=1
    if r+t>=2:
        print(f'#{num+1} 1')
    else:
        print(f'#{num+1} 0')