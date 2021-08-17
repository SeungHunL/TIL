def my_count(a, b):
    count = 0
    for i in b:
        if a == i:
            count += 1
    return count


def my_max(mmax, n):
    if mmax < n:
        mmax = n
    return mmax


T = int(input())
for _ in range(T):
    A = list(set(input()))
    B = input()

    mx = 0
    for i in A:
        mx = my_max(mx, my_count(i, B))
    print(f'#{_ + 1} {mx}')
