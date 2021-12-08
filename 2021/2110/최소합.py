def follow(arr, sy, sx, exp):
    global cost
    exp += arr[sy][sx]
    if sy == N - 1 and sx == N - 1:
        if cost < exp:
            cost = exp
        return
    elif sy + 1 < N and sx + 1 < N:
        if arr[sy + 1][sx] > arr[sy][sx + 1]:
            sx += 1
        elif arr[sy + 1][sx] < arr[sy][sx + 1]:
            sy += 1
        else:
            follow(arr, sy, sx + 1, exp)
            follow(arr, sy + 1, sx, exp)
            return
    elif sy + 1 == N:
        sx += 1
    elif sx + 1 == N:
        sy += 1
    follow(arr, sy, sx, exp)


for q in range(int(input())):
    N = int(input())
    board = []
    for w in range(N):
        board.append(list(map(int, input().split())))
    cost = 0
    follow(board, 0, 0, 0)
    print(f'#{q+1} {cost}')
