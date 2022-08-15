import sys


def calc(arr):
    ans = 0
    for i in range(N):
        h = arr[i]
        tmp = 0
        slope_left = []
        for j in range(i):
            slope_left.append((h - arr[j]) / (i - j))
        ml = None
        for k in range(len(slope_left)-1,-1,-1):
            if k==-1: break
            if ml is None or slope_left[k] < ml:
                ml = slope_left[k]
                tmp += 1

        slope_right = []
        for j in range(i + 1, N):
            slope_right.append((h - arr[j]) / (i - j))

        mr = None
        for k in range(len(slope_right)):
            if mr is None or slope_right[k] > mr:
                mr = slope_right[k]
                tmp += 1
        ans = max(tmp, ans)
    print(ans)


input = sys.stdin.readline
N = int(input())
buildings = list(map(int, input().split()))
calc(buildings)
