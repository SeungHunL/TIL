import sys

input= sys.stdin.readline

N=int(input())
nums=[[] for _ in range(50)]
for i in range(N):
    w=input().strip()[::-1]
    for j in range(len(w)):
        nums[j].append(w[j])
K=int(input())
kk=set()
for i in range(50):
    t=set(nums[-i-1])
    if t:
        if K>=len(t-kk):
            kk+=t
            K=len(kk)
            if K==0:
                break
        else:
            a=t-kk
            for j in a:
                
            break
print(nums)
