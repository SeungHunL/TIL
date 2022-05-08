import sys


def equ_r(arr):
    narr = []
    for line in arr:
        elements = set(line)
        if 0 in elements:
            elements.remove(0)
        nline = [(element, line.count(element)) for element in sorted(list(elements))]
        nline.sort(key=lambda x: x[1])
        line = []
        for t in nline:
            line += list(t)
        narr.append(line)
    arr_len = max(list(map(len, narr)))
    for i in range(len(narr)):
        narr[i] += (arr_len - len(narr[i])) * [0]
        if len(narr[i]) > 100:
            narr[i] = narr[i][:100]
    return narr


def equ_c(arr):
    narr = []
    for line in zip(*arr):
        elements = set(line)
        if 0 in elements:
            elements.remove(0)
        nline = [(element, line.count(element)) for element in sorted(list(elements))]
        nline.sort(key=lambda x: x[1])
        line = []
        for t in nline:
            line += list(t)
        narr.append(line)
    arr_len = max(list(map(len, narr)))
    for i in range(len(narr)):
        narr[i] += (arr_len - len(narr[i])) * [0]
        if len(narr[i]) > 100:
            narr[i] = narr[i][:100]
    return list(map(list, zip(*narr)))

input = sys.stdin.readline

r, c, k = map(int, input().split())
r -= 1
c -= 1
A = [list(map(int, input().split())) for _ in range(3)]
time = 0
while True:
    if 0 <= r < len(A) and 0 <= c < len(A[0]) and A[r][c] == k:
        print(time)
        break
    elif time > 100:
        print(-1)
        break
    h = len(A)
    w = len(A[0])

    if h >= w:
        A = equ_r(A)
    else:
        A = equ_c(A)

    time += 1
