zeros=[1,2,3,4,5]
used=[]
cnt=0
for a in zeros:
    zeros.remove(a)
    used=[]
    for b in zeros:
        used.append(b)
        for c in zeros:
            if c not in used:
                cnt+=1
                print(a,b,c)
print(cnt)