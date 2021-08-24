def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    print(arr)
    pivot = arr[len(arr) // 2]
    less, equal, more = [], [], []
    for i in arr:
        if pivot == i:
            equal.append(i)
        elif pivot > i:
            less.append(i)
        else:
            more.append(i)
    return quick_sort(less) + equal + quick_sort(more)


print(quick_sort([1, 6, 4, 3, 3, 5, 7]))
