def fp(n):
    ans=[]
    while n!=1:
        n=t[n]
        ans.append(n)
    return ans

for q in range(int(input())):
    V,E,t1,t2=map(int,input().split())
    tlist=list(map(int,input().split()))
    p= {}
    t=[0]*(V+1)
    for i in range(E):
        if tlist[2*i]in p:
            p[tlist[2*i]]=p[tlist[2*i]]+[tlist[2*i+1]]
        else:
            p[tlist[2*i]]=[tlist[2*i+1]]
        t[tlist[2 * i + 1]] = tlist[2 * i]
    parent = list(set(fp(t1)) & set(fp(t2)))[-1]
    ans=[parent]
    m=[parent]
    while m:
        kid=m.pop()
        if kid in p:
            m+=p[kid]
            ans+=p[kid]
    print(f'#{q + 1} {parent} {len(ans)}')
