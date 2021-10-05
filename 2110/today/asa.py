def selectionsort(arr, l):
    for i in range(l - 1):
        minidx = i
        for j in range(i + 1, l):
            if arr[minidx][1] > arr[j][1]:
                minidx = j
        arr[minidx], arr[i] = arr[i], arr[minidx]


for tc in range(int(input())):
    n = int(input())
    container = []
    for _ in range(n):
        s, e = map(int, input().split())
        container.append((s, e))
    selectionsort(container, n)
    print(container)
    cnt = 0
    now = 0
    for t in container:
        if t[0] >= now:
            cnt += 1
            now = t[1]
    print(f'#{tc + 1} {cnt}')