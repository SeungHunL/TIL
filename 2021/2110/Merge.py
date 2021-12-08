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

