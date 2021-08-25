import sys

sys.stdin = open("input (1).txt", "r")
for _ in range(1):
    T = int(input())
    N = []
    for t in range(T):
        N.append(list(map(int, input().split())))
    for i in range(1):
        stack = []
        for j in range(T):
            stack.append(N[j][i])

        print(stack)
        for __ in range(1):
            move = 0
            for k in range(100):
                if stack[k] == 1:
                    if k == 99:
                        stack[k] = 0
                    elif stack[k + 1] == 0:
                        stack[k] = 0
                        stack[k + 1] = 1
                    move = 1
                elif stack[k] == 2:
                    if k == 0:
                        stack[k] = 0
                    elif stack[k - 1] == 0:
                        stack[k] = 0
                        stack[k + 1] = 1
                    move = 1
                print(stack)
            if not move:
                break
