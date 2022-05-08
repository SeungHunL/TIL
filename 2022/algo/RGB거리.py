import sys

input = sys.stdin.readline

N = int(input())
maps = [list(map(int, input().split())) for i in range(N)]
score = 1e9
idx = 0
ans = []
dp = []
for i in range(3):
    for j in range(3):
        if i != j and score > maps[0][i] + maps[1][j]:
            score = maps[0][i] + maps[1][j]
            idx = i
ans.append(idx)
dp.append(maps[0][idx])
for i in range(1, N - 1):
    score = 1e9
    for j in range(3):
        for k in range(3):
            if j != k and ans[-1] != j and score > dp[-1] + maps[i][j] + maps[i + 1][k]:
                score = dp[-1] + maps[i][j] + maps[i + 1][k]
                idx = j
    ans.append(idx)
    dp.append(dp[-1] + maps[i][idx])
score = 1e9
for i in range(3):
    if ans[-1] != i and score > dp[-1] + maps[-1][i]:
        score = dp[-1] + maps[-1][i]
        idx = i
dp.append(dp[-1] + maps[-1][idx])
print(dp[-1])
