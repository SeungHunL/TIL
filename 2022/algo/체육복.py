def solution(n, lost, reserve):
    st = [0] * (n + 2)
    for l in lost:
        st[l] = 1
    n_reserve = []
    for r in reserve:
        if st[r]:
            st[r] = 0
        else:
            n_reserve.append(r)
    n_reserve.sort()
    for r in n_reserve:
        if st[r - 1]:
            st[r - 1] = 0
        elif st[r + 1]:
            st[r + 1] = 0

    return n - st.count(1)