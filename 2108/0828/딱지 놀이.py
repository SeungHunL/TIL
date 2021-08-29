import sys

N = int(sys.stdin.readline())
for _ in range(N):
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    for i in range(4, -1, -1):
        if A[1:].count(i) > B[1:].count(i):
            print('A')
            break
        elif A[1:].count(i) < B[1:].count(i):
            print('B')
            break
        elif i == 0 and A[1:].count(i) == B[1:].count(i):
            print('D')
            break

