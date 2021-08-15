import sys
N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    A = list(sys.stdin.readline().split())

    if A[0] == 'push':
        stack.append(A[1])
    elif A[0] == 'top':
        print(stack[-1]) if len(stack) != 0 else print(-1)
    elif A[0] == 'size':
        print(len(stack))
    elif A[0] == 'empty':
        print(1 if len(stack) == 0 else 0 )
    elif A[0] == 'pop':
        print(-1 if len(stack) == 0 else stack.pop())

