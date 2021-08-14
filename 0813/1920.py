M = int(input())
A = list(map(int,input().split()))
N = int(input())
NL = list(map(int,input().split()))
for i in range(N):
    if NL[i]in A:
        print(1)
    else:
        print(0)