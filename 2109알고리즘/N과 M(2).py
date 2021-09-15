import sys


def backtracking(k):
    if k == M:
        for l in stack:
            print(l + 1, end=' ')
        print()
        return
    else:
        k += 1
        start = stack[-1] if stack else 0
        for i in range(start, N):
            if i not in used:
                used.append(i)
                stack.append(i)
                backtracking(k)
                used.pop()
                stack.pop()


N, M = map(int, sys.stdin.readline().split())

used = []
stack = []
backtracking(0)
