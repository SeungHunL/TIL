N = int(input())

for num in range(N):
    A = list(input().split())
    s = float(A[0])
    for i in range(1,len(A)):
        if A[i]=='@':
            s *= 3
        elif A[i] == '%':
            s += 5
        elif A[i] == '#':
            s -= 7
    print('%0.2f'%s)
