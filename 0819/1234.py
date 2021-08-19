def pw(L):
    N = len(L)
    for i in range(N - 1):
        k = 1
        while L[i] == L[i + 1]:
            if i - (k - 1) >= 0 and i + k <= N - 1 and L[i - k + 1] == L[i + k]:
                L[i - k + 1] = ''
                L[i + k] = ''
            else:
                break
            k += 1
    return L


for _ in range(10):
    a, b = input().split()
    size = int(a)
    Let = list(b)
    while 1:
        Let = pw(Let)
        if pw(Let) == Let:
            break

    print(f'#{_ + 1}', end=' ')
    for m in range(len(Let)):
        if Let[m]:
            print(Let[m], end='')
    print()