# for _ in range(int(input())):
#     cube = []
#     N = int(input())
#
#     for __ in range(N):
#         cube.append(list(map(int, input().split())))

def comb(arr, sel, idx, s_idx, R):
    if s_idx == R:
        print(sel)
        return
    elif idx == len(arr):
        return
    else:
        sel[s_idx] = arr[idx]
        comb(arr, sel, idx + 1, s_idx+1, R)
        comb(arr, sel, idx + 1, s_idx, R)


A=[]
N=3
for i in range(N):
    A.append(i)
S = [0] * N
comb(A, S, 0, 0, N)
