import sys

input= sys.stdin.readline

N=int(input())
times=[]
for i in range(N):
    times.append(list(map(int,input().split())))
times.sort(key=lambda x:(x[1],x[0]))

tmp=1
et=times[0][1]
for i in range(1,N):
    s,e= times[i][0],times[i][1]
    if s>=et:
        tmp+=1
        et=e
print(tmp)