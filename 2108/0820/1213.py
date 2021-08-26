import sys


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    less, equal, more = [], [], []
    for i in arr:
        if i < pivot:
            less.append(i)
        elif i == pivot:
            equal.append(i)
        else:
            more.append(i)
    return quick_sort(less) + equal + quick_sort(more)


L = quick_sort(list(sys.stdin.readline().strip()))
ans, reverse, mid, k = [], [], [], 0

while k < len(L):
    if k < len(L) - 1 and L[k] == L[k + 1]:
        ans.append(L[k])
        reverse.append(L[k])
        k += 2
    else:
        mid.append(L[k])
        k += 1
if len(mid) > 1:
    print("I'm Sorry Hansoo")
else:
    print(''.join(ans + mid + reverse[::-1]))
