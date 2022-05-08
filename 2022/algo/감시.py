import sys


def find_cube(arr):
    global ans
    check = [ma[:] for ma in maps]
    for i in range(len(arr)):
        for dy, dx in D[cctv[i][0] - 1][arr[i]]:
            y, x = cctv[i][1]
            while 1:
                y, x = y + dy, x + dx
                if 0 <= y < N and 0 <= x < M:
                    if check[y][x] == 0 :
                        check[y][x] = '#'
                    elif check[y][x] == 6:
                        break
                else:
                    break
    # for c in check:
    #     print(c)
    # print()
    ans = min(ans, sum(list(map(lambda x: x.count(0), check))))


def make_arr(arr):
    if len(arr) == len(cctv):
        find_cube(arr)
    else:
        for i in range(len(D[cctv[len(arr)][0] - 1])):
            arr.append(i)
            make_arr(arr)
            arr.pop()


input = sys.stdin.readline

N, M = map(int, input().split())
D = [
    [[(-1, 0)], [(0, 1)], [(1, 0)], [(0, -1)]],
    [[(-1, 0), (1, 0)], [(0, 1), (0, -1)]],
    [[(-1, 0), (0, 1)], [(-1, 0), (0, -1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)]],
    [[(0, 1), (1, 0), (0, -1)], [(-1, 0), (1, 0), (0, -1)], [(-1, 0), (0, 1), (0, -1)], [(-1, 0), (0, 1), (1, 0)]],
    [[(-1, 0), (0, 1), (1, 0), (0, -1)]],
]
maps = [list(map(int, input().split())) for _ in range(N)]
cctv = []
ans = 1e9
for i in range(N):
    for j in range(M):
        if 0 < maps[i][j] < 6:
            cctv.append([maps[i][j], (i, j)])
make_arr([])
if not cctv:
    ans = sum(list(map(lambda x: x.count(0), maps)))
print(ans)
