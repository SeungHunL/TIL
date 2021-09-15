from sys import stdin
T = int(stdin.readline())
for _ in range(T):
    A, B = map(int,stdin.readline().split())
    if A > B:
        mn, mx = B, A
    else:
        mn, mx = A, B
    for i in range(1, mn + 1):
        if (mx*i) % mn == 0:
            print(mx*i)
            break
