import sys


def nqueen(board, t):
    global s
    if t == n:
        s += 1
        return
    for i in range(n):
        for j in range(i):
            if board[j] == i or i - j == abs(board[j] - i):
                return
        board[t] = i
        nqueen(board, t + 1)


input = sys.stdin.readline

n = int(input())
maps = [0] * n
s = 0
nqueen(maps, 0)
print(s)
