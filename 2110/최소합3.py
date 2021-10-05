def follow(arr):
    for i in range(1,2*N):
        for j in range(i+1):
            print(j,i-j)
            if arr[j-1][i-j]>arr[j][i-j-1]:
                arr[j][i-j]+=arr[i][i-j+1]

for q in range(int(input())):
    N = int(input())
    board = []
    for w in range(N):
        board.append(list(map(int, input().split())))
    follow(board)
    print(board)
    # print(f'#{q+1} {cost}')
