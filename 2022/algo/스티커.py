import sys

input = sys.stdin.readline

for _ in range(int(input())):
    maps = []
    n = int(input())
    for p in range(2):
        maps.append(list(map(int, input().split())))
    if maps[0][0] >maps[0][1]:
        dp=[[1,maps[0][0]]]
    else:
        dp=[[2,maps[1][0]]]
    for i in range(1,n):
        if dp[-1][1]==1:
            if dp[-1][2]+dp[-1][]
            dp.append([2,])
