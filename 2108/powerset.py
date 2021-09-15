def powerset(idx, N, sel):
    if idx == N:
        print(sel)
    else:
        sel[idx] = 1
        powerset(idx + 1, N, sel)
        sel[idx] = 0
        powerset(idx + 1, N, sel)


N = 3
sel = [0] * N
powerset(0, N, sel)
