for i in range(10):
    T = int(input())
    N = list(map(int, input().split()))
    front = rear = 0
    n = 0
    while 1:
        N[front] -= (n + 1)
        if N[front] <= 0: N[front] = 0; break
        front += 1
        front %= len(N)
        n += 1
        n %= 5
    ans = N[front + 1:] + N[:front + 1]
    ans = ' '.join(map(str, ans))
    print(f'#{i + 1} {ans}')
