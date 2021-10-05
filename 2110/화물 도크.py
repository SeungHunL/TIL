def quick(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[len(arr)//2][0]
    l,e,h=[],[],[]
    for num in arr:
        if num[0] >pivot:
            h.append(num)
        elif num[0]==pivot:
            e.append(num)
        else:
            l.append(num)
    return quick(l)+e+quick(h)

def perm(arr,s=0,cnt=0,hour=0):
    global time,use
    if cnt==1:
        use[s]=1
    if time<cnt:
        time=cnt
    for i in range(s, len(arr)):
        if arr[i][0]>=hour and not use[i]:
            perm(arr, i,cnt+1,arr[i][1])

for q in range(int(input())):
    N =int(input())
    tt=[]
    for i in range(N):
        tt.append(list(map(int,input().split())))
    tt=quick(tt)
    time=0
    use=[0]*N
    perm(tt)
    print(f'#{q + 1} {time}')
