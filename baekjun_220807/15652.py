import sys

def func(num,last):
    global ans
    if num==M:
        print(' '.join(list(map(str,ans))))
        return
    for i in range(last,N+1):
        ans.append(i)
        func(num+1,i)
        ans.pop()

input = sys.stdin.readline

N,M=map(int,input().split())
ans=[]
func(0,1)