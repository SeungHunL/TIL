import sys

N = int(sys.stdin.readline())
T = int(sys.stdin.readline())
apple = []
for _ in range(T):
    apple.append(list(map(int, sys.stdin.readline().split())))

L = int(sys.stdin.readline())

trace = [[0, 0]]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
k = 0
x, y = -1, 0
s = -1
flag = 0
for l in range(L):
    X, C = map(str, sys.stdin.readline().split())
    X = int(X)

    while s < X:
        x += dx[k % 4]
        y += dy[k % 4]

        if len(trace) > 2 and [y, x] in trace:
            flag +=1
            break

        trace.append([y, x])

        for a in range(len(apple)):
            if apple[a] == [x, y]:
                print('apple')
                break
        else:
            trace.pop(0)

        if 0 <= x <= N and 0 <= y <= N:
            pass
        else:
            flag+=1
            break

        s += 1
        print(s, y, x)
    print(trace)
    if s < X - 1 or flag>0:
        # print(s,X-1,'break')
        print(s)
        break
    if C == 'L':
        k -= 1
    else:
        k += 1
