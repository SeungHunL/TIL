T=int(input())
for _ in range(T):
    N=int(input())
    taken=[0]*N
    for i in range(N):
        taken[i]= list(map(int,input().split()))
    