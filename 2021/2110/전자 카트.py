def perm(num, use, t=0, path=[]):
    global expense
    if t == num - 1:
        if expense > cost(path):
            expense = cost(path)
            return
    for i in range(1, num):
        if not use[i]:
            path.append(i)
            use[i] = 1
            perm(num, use, t + 1, path)
            path.pop()
            use[i] = 0


def cost(arr):
    total = board[0][arr[0]]
    for i in range(len(arr) - 1):
        total += board[arr[i]][arr[i + 1]]
    total += board[arr[-1]][0]
    return total


for q in range(int(input())):
    N = int(input())
    expense = 1000000
    board = []
    for w in range(N):
        board.append(list(map(int, input().split())))
    perm(N, [0] * N)
    print(f'#{q + 1} {expense}')
