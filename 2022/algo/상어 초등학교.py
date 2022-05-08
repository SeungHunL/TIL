import sys

input = sys.stdin.readline


def find_empty():
    max_c = 0
    for y in range(N):
        for x in range(N):
            if maps[y][x] == 0:
                c = 1
                for dy, dx in d:
                    ty, tx = y + dy, x + dx
                    if 0 <= ty < N and 0 <= tx < N:
                        c += 1
                if max_c < c:
                    if c == 5:
                        maps[y][x] = s_num
                        seat[s_num] = (y, x)
                        return
                    max_c = c
                    my, mx = y, x
    maps[my][mx] = s_num
    seat[s_num] = (my, mx)


def find_seat():
    goto = []
    for key, value in doto.items():
        if value == level:
            goto.append(key)
    max_c = 0
    goto.sort()
    for y, x in goto:
        c = 1
        for dy, dx in d:
            ty, tx = y + dy, x + dx
            if 0 <= ty < N and 0 <= tx < N and (maps[ty][tx] == 0):
                c += 1
        if max_c < c:
            if c == 5:
                maps[y][x] = s_num
                seat[s_num] = (y, x)
                return
            max_c = c
            my, mx = y, x
    maps[my][mx] = s_num
    seat[s_num] = (my, mx)


N = int(input())
maps = [[0] * N for _ in range(N)]
seat = [(0, 0)] * (N ** 2 + 1)
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
students = []
for _ in range(N ** 2):
    student = list(map(int, input().split()))
    students.append(student)
    s_num = student[0]
    s_like = student[1:]
    doto = {}
    level = 0
    for i in s_like:
        if seat[i]:  # x,y
            y, x = seat[i]
            for dy, dx in d:
                ty, tx = y + dy, x + dx
                if 0 <= ty < N and 0 <= tx < N and (maps[ty][tx] == 0):
                    if (ty, tx) not in doto:
                        doto[(ty, tx)] = 1
                    else:
                        doto[(ty, tx)] += 1
                    if doto[(ty, tx)] > level:
                        level = doto[(ty, tx)]

    if level == 0:
        find_empty()
    else:
        find_seat()
ans = 0
for s in students:
    y, x = seat[s[0]]
    c = 0
    for dy, dx in d:
        ty, tx = y + dy, x + dx
        if 0 <= ty < N and 0 <= tx < N and (maps[ty][tx] in s[1:]):
            c += 1
    ans += (10 ** (c - 1)) if c else 0
print(ans)
# for m in maps:
#     print(m)
