def comb(arr,use=[],ans=[]):
    if len(ans)==6:
        ans=''.join(ans)
        things.add(ans)
        return
    if not use:
        use = [0] * len(arr)
    for i in range(len(arr)):
        if not use[i]:
            ans.append(str(arr[i]))
            use[i]=1
            comb(arr,use,ans)
            ans.pop()
            use[i]=0

def babyjin(st):
    for i in st:
        if int(i[0])==int(i[1])-1 and int(i[2])==int(i[1])+1 and len(set(i[3:]))==1:
            return 1
        elif len(set(i[:3]))==1 and int(i[3])==int(i[4])-1 and int(i[5])==int(i[4])+1:
            return 1
    return 0

things=set()
comb([1,2,3,7,7,7])
print(babyjin(things))