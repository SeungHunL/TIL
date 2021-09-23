part = []


def dfs(arr, n):
    if len(part) == n:
        return part
    
T = int(input())
for _ in range(T):
    oned, onem, threem, oney = map(int, input().split())
    cal = list(map(int, input().split()))
    mn=100000
    calp=cal[:]

    # 1일 1달 비교
    for i in range(12):
        if cal[i]:
            if onem< oned*cal[i]:
                cal[i]=onem
            else:
                cal[i]=oned*cal[i]

    # 1달 3달 비교
    total=0
    nlist=[]
    for j in range(9):
        if calp[i]+calp[i+1]+calp[i+2]>threem:
            nlist.append(i)

    if len(nlist)>2:
        for k in range(2,len(nlist)):
            if dfs(arr,k)







