def quick(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    l, e, h = [], [], []
    for num in arr:
        if num > pivot:
            h.append(num)
        elif num == pivot:
            e.append(num)
        else:
            l.append(num)
    return quick(l) + e + quick(h)


for q in range(int(input())):
    N, M = map(int, input().split())
    con = quick(list(map(int, input().split())))[::-1]
    truck = quick(list(map(int, input().split())))[::-1]
    total = 0
    for i in range(len(con)):
        for j in range(len(truck)):
            if truck[j] >= con[i]:
                truck[j] = 0
                total += con[i]
                break

    print(f'#{q + 1} {total}')
