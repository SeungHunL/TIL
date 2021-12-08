# def perm(arr, sel, check, idx, N):
#     if idx == N:
#         print(sel)
#         return
#     else:
#         for i in range(N):
#             if check[i] == 0:
#                 sel[idx] = arr[i]
#                 check[i] = 1
#                 perm(arr, sel, check, idx + 1, N)
#                 check[i] = 0
def perm(arr, sel, check, load, idx, N):
    if idx == N:
        path.append(sel)
        return
    else:
        for i in range(N):
            if check[i] == 0:
                sel[idx] = arr[i]
                check[i] = 1
                perm(arr, sel, check, load, idx + 1, N)
                check[i] = 0


arr = [1, 2, 3]
N = len(arr)
sel = [0] * N
check = [0] * N
path = []

A = [[2, 1, 2],
     [5, 8, 5],
     [7, 2, 2]]
perm(arr, sel, check, path, 0, N)
print(path)
