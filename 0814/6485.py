T = int(input())
for _ in range(T):
    N = int(input())
    count = {}
    for n in range(N):
        A, B = map(int, input().split())
        for i in range(A,B+1):
            count[i] = count.get(i,0)+1

    P = int(input())
    result = {}

    print('#{}'.format(_ + 1), end=' ')
    for k in range(P):
        a = int(input())
        if count.get(a):
            print("{}".format(count[a]), end=" ")
        else:
            print("0", end =' ')
    print()