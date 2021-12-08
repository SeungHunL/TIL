import sys

T = int(sys.stdin.readline())


def my_min(arr):
    for i in range(0, len(arr)):
        if i == 0:
            mi = arr[0]
            min_idx = 0
        elif mi > arr[i]:
            mi = arr[i]
            min_idx = i
    return min_idx


Emp_l = []
for _ in range(T):
    N = int(sys.stdin.readline())
    if N:
        Emp_l.append(N)
    else:
        if Emp_l:
            mi = my_min(Emp_l)
            print(Emp_l[mi])
            del Emp_l[mi]
        else:
            print(0)
