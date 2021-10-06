def Mergesort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    return merge(Mergesort(arr[:mid]),Mergesort(arr[mid:]))

def merge(L,R):
    global a
    ans=[0]*(len(L)+len(R))
    s1,s2=len(L)-1,len(R)-1
    i=len(ans)-1
    flag=0
    while 0<=s1 and 0<=s2:
        if L[s1]<=R[s2]:
            ans[i]=R[s2]
            s2-=1
        else:
            if not flag:
                a+=1
            ans[i] = L[s1]
            s1 -= 1
        i-=1
        flag=1
    while 0<=s1:
        ans[i] = L[s1]
        i -= 1
        s1 -= 1
    while 0<=s2:
        ans[i] = R[s2]
        i -= 1
        s2 -= 1
    return ans

for q in range(int(input())):
    N=int(input())
    T=list(map(int,input().split()))
    a=0
    T=Mergesort(T)
    print(f'#{q+1} {T[len(T)//2]} {a}')

def mergesort(a, left, right):
    if left == right:
        return a


    mid = (left + right) // 2
    l = mergesort(a[left:mid], left, mid)
    r = mergesort(a[mid:right], mid, right)
    return merge(l, r)


def merge(l, r):
    global cnt
    res = []
    i = 0  # left idx
    j = 0  # right idx
    while i < len(l) or j < len(r):
        if i < len(l) and j < len(r):
            if l[i] <= r[j]:
                res.append(l[i])
                i += 1
            else:
                res.append(r[j])
                j += 1
        elif i >= len(l):
            while j < len(r):
                res.append(r[j])
                j += 1
        else:
            cnt += 1
            while i < len(l):
                res.append(l[i])
                i += 1
    return res


for tc in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    mergesort(arr, 0, n)
    print(f'{tc + 1} {arr[n // 2]} {cnt}')