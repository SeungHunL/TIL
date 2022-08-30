import sys

def func(arr):
    for i in range(N):
        if i == 0:
            pass
        else:
            for j in range(1, i + 1):
                if board[i - j] < board[i]:
                    arr[i] = max(arr[i], arr[i - j] + 1)
                elif board[i - j] == board[i]:
                    arr[i] = max(arr[i], arr[i - j])
                    break
    return arr

input = sys.stdin.readline

N=int(input())
board=list(map(int,input().split()))
if N==1:
    print(1)
else:

    dp=func([1]*N)
    board=board[::-1]
    dp2=func([1]*N)[::-1]

    res=[0]*N
    for i in range(N):
        res[i]=dp[i]+dp2[i]-1
    print(max(res))