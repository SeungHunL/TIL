def comb(arr, arr2, sel, idx, s_idx, R, total):
    n = 1
    if s_idx == R:
        for i in range(R):
            total
        print(sel)
        return
    elif idx == len(arr):
        return
    else:
        sel[s_idx] = arr[idx]
        n += 1
        comb(arr, arr2, sel, idx + 1, s_idx + 1, R, total)
        comb(arr, arr2, sel, idx + 1, s_idx, R, total)

for _ in range(int(input())):
    N = int(input())
    cube = []
    for __ in range(N):
        cube.append(list(map(int, input().split())))
#
#     total = 0
#     M_total = 1000000
#     min_idx = 0
#     stack = []
#     check = []
#
#     for j in range(N):
#
#         for k in range(N):
#             if k not in check:
#                 min_idx = k
#                 break
#
#         for i in range(N):
#             if cube[j][min_idx] > cube[j][i] and (i not in check):
#                 min_idx = i
#             elif cube[j][min_idx] == cube[j][i] and (i not in check)
#                 stack.append(i)
#         check.append(min_idx)
#         total += cube[j][min_idx]
#     if M_total > total:
#         M_total = total
#     print(f'#{_ + 1} {M_total}')
