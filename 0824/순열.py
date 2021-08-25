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