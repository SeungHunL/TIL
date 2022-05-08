import sys

input = sys.stdin.readline

N = int(input())
maps = [[0] * N for _ in range(N)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
students = [[] for _ in range(N ** 2 + 1)]
seated = {}
for _ in range(N ** 2):
    flag=0
    check = [[0] * N for _ in range(N)]
    student = list(map(int, input().split()))
    students[student[0]] = student[1:]
    # 좋아하는 사람 옆자리 체크
    for i in student[1:]:
        if i in seated:
            y, x = seated[i]
            for dy, dx in d:
                ty, tx = y + dy, x + dx
                if 0 <= ty < N and 0 <= tx < N and maps[ty][tx] == 0:
                    check[ty][tx] += 1
    liked = max(list(map(max, check)))
    if liked > 0:  # 좋아하는 사람이 자리에 있을 때
        arr = []
        for i in range(N):
            for j in range(N):
                if check[i][j] == liked:
                    arr.append((i, j))
        if len(arr) > 1:  # 자리가 여럿 있을 때
            score = -1
            for y, x in arr:  # 빈 자리가 젤 많은 장소 찾기
                c = 0
                for dy, dx in d:
                    ty, tx = y + dy, x + dx
                    if 0 <= ty < N and 0 <= tx < N and maps[ty][tx] == 0:
                        c += 1
                if score < c:
                    score = c
                    ay, ax = y, x
        else:  # 자리가 하나 일 때
            ay, ax = arr.pop()
    else:
        score = -1
        for y in range(N):
            if flag:
                break
            for x in range(N):
                if not maps[y][x]:
                    c = 0
                    for dy, dx in d: # 주변에 빈자리 찾기
                        ty, tx = y + dy, x + dx
                        if 0 <= ty < N and 0 <= tx < N and maps[ty][tx] == 0:
                            c += 1
                    if c == 4:
                        ay, ax = y, x
                        flag=1
                        break
                    elif score < c:
                        score = c
                        ay, ax = y, x
    maps[ay][ax] = student[0]
    seated[student[0]] = (ay, ax)
ans = 0
for key, value in seated.items():
    y, x = value
    c = 0
    for dy, dx in d:
        ty, tx = y + dy, x + dx
        if 0 <= ty < N and 0 <= tx < N and (maps[ty][tx] in students[key]):
            c += 1
    ans += (10 ** (c - 1)) if c else 0
print(ans)
