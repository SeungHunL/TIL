import sys

input = sys.stdin.readline

T = int(input())
color=[]
for _ in range(T):
    color.append(list(map(int, input().split())))

# for i in range(3):
cost = [1001] * T
rgb = [0] * T
for x in range(3):
    for y in range(3):
        if x!=y:
            a = color[0][x]+color[1][y]
            if a <cost[1]:
                cost[1]=a
                rgb[1]=y
for j in range(2, T):
    for k in range(3):
        if k != rgb[j - 1]:
            if cost[j - 1] + color[j][k] < cost[j]:
                cost[j] = cost[j - 1] + color[j][k]
                rgb[j]=k

print(cost[T-1])