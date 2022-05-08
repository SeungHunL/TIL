import sys

input = sys.stdin.readline

N = int(input())
ans = N // 5
while 1:
    a = (N - ans * 5) % 3
    if a == 0:
        print(ans + (N - ans * 5) // 3)
        break
    elif ans:
        ans -= 1
    else:
        print(-1)
        break
