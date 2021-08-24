N = 3
arr = [1, 2, 3]
sel = [0] * N
check = [0] * N
ans = []


def perm(arr, sel, check, idx, N, ans):
    if idx == N:
        ans.append(sel)
        return ans
    else:
        for i in range(N):
            if check[i] == 0:
                sel[idx] = arr[i]
                check[i] = 1
                perm(arr, sel, check, idx + 1, N, ans)
                check[i] = 0


perm(arr, sel, check, 0, N, ans)
print(ans)
