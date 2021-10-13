for q in range(10):
    V,E=map(int,input().split())
    tlist=list(map(int,input().split()))
    d={}
    for i in range(E):
        if tlist[2*i+1]in d:
            d[tlist[2*i+1]]=d[tlist[2*i+1]]+[tlist[2*i]]
        else:
            d[tlist[2*i+1]]=[tlist[2*i]]
    print(d)