def perm(arr, sel, check, idx, N, target):
    global X
    if idx == N:
        sel_sum = 0
        for k in range(len(sel)):
            sel_sum += target[k][sel[k]]
        if X > sel_sum:
            X = sel_sum
        return
    else:
        for i in range(N):
            if check[i] == 0:
                sel[idx] = arr[i]
                check[i] = 1
                perm(arr, sel, check, idx + 1, N, target)
                check[i] = 0


for _ in range(int(input())):
    N = int(input())
    I = [];
    for __ in range(N): I.append(__)
    A = [];
    for ___ in range(N): A.append(list(map(int, input().split())))
    S = [0] * N
    check = [0] * N
    X = 1000000000
    perm(I, S, check, 0, N,A)
    print(f'#{_+1} {X}')
