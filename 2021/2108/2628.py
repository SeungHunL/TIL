N, M = map(int, input().split())
T = int(input())
K = [0] * T
garo = [0] * N
selo = [0] * M
for _ in range(T):
    K[_] = list(map(int, input().split()))
for i in range(T):
    if K[i][0] == 0:
        selo[K[i][1]] += 1
    else:
        garo[K[i][1]] += 1
count = 0
ymax = 0
for j in range(M):
    if selo[j]:
        count += 1
    else:
        if ymax < count:
            ymax = count
        count = 1
print(ymax,selo)
count = 0
xmax = 0
for k in range(N):
    if garo[k]:
        count += 1
    else:
        if xmax < count:
            xmax = count
        count = 0
print(xmax*ymax)