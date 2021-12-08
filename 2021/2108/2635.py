N = int(input())
mx = 0
for i in range(1, N+1):
    S = [N, i]
    while 1:
        if (S[-2] - S[-1]) >= 0:
            S.append(S[-2] - S[-1])
        else:
            break
    if mx < len(S):
        mx = len(S)
        mxlist = S
print(mx)
for k in range(mx):
    print(mxlist[k], end=' ')
