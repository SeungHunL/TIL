def in_order(arr, v):
    if arr[v]:
        if len(arr[v]) > 2:
            in_order(arr, int(arr[v][2])-1)
        print(arr[v][1],end='')
        if len(arr[v]) > 3:
            in_order(arr, int(arr[v][3])-1)


for _ in range(10):
    N = int(input())
    film = []
    for __ in range(N):
        film.append(list(input().split()))
    print(f'#{_+1}',end=' ')
    in_order(film,0)
    print()